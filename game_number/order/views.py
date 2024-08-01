from django.shortcuts import get_object_or_404  
from rest_framework.decorators import api_view ,authentication_classes
from rest_framework.response import Response  
from rest_framework import status  
from .models import orders,RW_Order
from rest_framework.authentication import TokenAuthentication 
from .serializers import OrderSerializer,RW_OrderSerializer
from goods.models import Product
from django.db import transaction
from django.db.models import F
from user.models import User
from django.http import HttpResponse,JsonResponse
from alipay import AliPay, AliPayConfig
from django.conf import settings
# 单个购买
@api_view(['POST'])  
def make_order(request):  
    # 改进错误处理和效率  
    product_id = request.data.get('product_id')  
    buyer = request.data.get('buyer')  
  
    # 使用get_object_or_404来优雅地处理无效的产品ID  
    product = get_object_or_404(Product, pk=product_id)  
  
    if product.is_saled:  
        # 如果产品已经售出，则返回一个有意义的错误响应  
        return Response({'error': '该产品已经售出。'}, status=status.HTTP_400_BAD_REQUEST)  
    buyer_obj = User.objects.get(username=buyer)
    # 获取购买者的余额和商品价格
    buyer_balance = buyer_obj.account_balance
    product_price = product.product_price

    # 检查购买者余额是否足够购买商品
    if buyer_balance < product_price:
        return Response({'error': '购买者余额不足。'}, status=status.HTTP_400_BAD_REQUEST)

    # 减去购买者的余额
    new_balance = buyer_balance - product_price
    buyer_obj.account_balance = new_balance
    buyer_obj.save()
    # 标记产品为已售  
    product.is_saled = True  
    product.save()  
      # 为购买者的购买数量加一
    User.objects.filter(username=buyer).update(purchased_quantity=F('purchased_quantity') + 1)
    # 为售卖者的售出数量加一
    User.objects.filter(username=product.user_id.username).update(sold_quantity=F('sold_quantity') + 1)
    

    order_data = {  
        'upper': product.user_id.username,  
        'buyer': buyer,  
        'product_id': product.product_id  # 向序列化器传递产品ID  
    }  

    serializer = OrderSerializer(data=order_data)  
    if serializer.is_valid():  
        serializer.save()  # 这将创建Order对象  
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
    else:  
        # 如果数据无效，返回一个400响应和错误详情  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    



@api_view(['POST'])  
def make_orders(request):  
    errors = []
    orders_data = []
    
    # 开始事务
    with transaction.atomic():
        products = request.data.get('productList', [])
        buyer = request.data.get('buyer')

        for product_id in products:
            product = get_object_or_404(Product, pk=product_id)

            if product.is_saled:  
                errors.append({'product_id': product_id, 'error': '该产品已经售出。'})
                continue

            product.is_saled = True  
            product.save()

            # 获取购买者对象
            buyer_obj = User.objects.get(username=buyer)
            # 获取购买者的余额和商品价格
            buyer_balance = buyer_obj.account_balance
            product_price = product.product_price

            # 检查购买者余额是否足够购买商品
            if buyer_balance < product_price:
                errors.append({'product_id': product_id, 'error': '购买者余额不足。'})
                continue

            # 减去购买者的余额
            new_balance = buyer_balance - product_price
            buyer_obj.account_balance = new_balance
            buyer_obj.save()

            # 购买者购买数量+1
            buyer_obj.purchased_quantity = F('purchased_quantity') + 1
            buyer_obj.save()

            # 为售卖者的售出数量加一
            seller_obj = product.user_id
            seller_obj.sold_quantity = F('sold_quantity') + 1
            seller_obj.save()

            order_data = {  
                'upper': seller_obj.username,  
                'buyer': buyer,  
                'product_id': product_id  
            }
            orders_data.append(order_data)

        # 在循环外部序列化订单
        serializers = [OrderSerializer(data=data) for data in orders_data]
        valid_serializers = []
        for serializer in serializers:
            if serializer.is_valid():
                valid_serializers.append(serializer)
            else:
                errors.append(serializer.errors)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            for serializer in valid_serializers:
                serializer.save()

            return Response([serializer.data for serializer in valid_serializers], status=status.HTTP_201_CREATED)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_rw_orders(request):
    user = request.user
    orders = RW_Order.objects.filter(user=user,is_recharge = False)
    print(orders)
    serializer = RW_OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



# 提现订单
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def create_rw_order(request):
    print(request.data)
    user = request.user
    amount = request.data.get('amount', 0)
    user_account = request.data.get('auth_account', '')

    rw_order_data = {
        'user': user,
        'is_recharge': False,
        'amount': amount,
        'user_account': user_account 
    }

    serializer = RW_OrderSerializer(data=rw_order_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)