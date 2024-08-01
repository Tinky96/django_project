from user.models import User
from rest_framework.response import Response
from rest_framework.authtoken.views import APIView,AuthTokenSerializer
from rest_framework.authtoken.models import Token
from .models import User 
from django.contrib.auth import authenticate
from rest_framework import status  
from rest_framework.response import Response  
from rest_framework.authtoken.models import Token  
from rest_framework.decorators import api_view, permission_classes,authentication_classes 
from rest_framework.permissions import AllowAny  
from .serializers import UserSerializer ,UserMessageSerializer
from rest_framework.authentication import TokenAuthentication
from django.conf import settings
from alipay import AliPay
import traceback
from order.models import RW_Order
from decimal import Decimal
from django.http import JsonResponse
# 用户注册  
@api_view(['POST'])   
@permission_classes((AllowAny,))  
def register_user(request):  
    serializer = UserSerializer(data=request.data)  
    if serializer.is_valid():  
        user = serializer.save()  
        token, created = Token.objects.get_or_create(user=user)  
        return Response({  
            'status': 'success',  
            'token': token.key,  
            'user_id': user.pk,  
        }, status=status.HTTP_201_CREATED)  
    else:  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
  
# 用户登录  
# 注意：用户登录通常不会创建一个新用户，而是验证现有用户的凭据。  
# 这里省略了登录视图的实现，因为它通常需要使用Django的认证系统。

@api_view(['POST'])  
@permission_classes((AllowAny,))  
def login_user(request):  
    print(request.data)
    username = request.data.get('username')  
    password = request.data.get('password')  
      
    if username is not None and password is not None:  
        user = authenticate(request, username=username, password=password)  
        if user is not None:  
            # 用户认证成功，创建或获取token  
            token, created = Token.objects.get_or_create(user=user)  
            print(token.key)
            return Response({  
                'status': 'success',  
                'user_id': user.pk,  
                'token': token.key,  
            }, status=status.HTTP_200_OK)  
        else:  
            # 用户名或密码错误  
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  
    else:  
        # 缺少用户名或密码  
        return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_user_info(request):
    user = request.user
    serializer = UserMessageSerializer(user)
    return Response(serializer.data)



# 充值
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def recharge(request):
    amount = request.data.get('amount')
    user = request.user
    try:
        recharge_order = RW_Order.objects.create(user = user,is_recharge = True,amount = amount)
        alipay = AliPay(
            appid=settings.ALIPAY_APPID,
            app_notify_url=None,  # 默认回调url
            app_private_key_string=open(settings.APP_PRIVATE_KEY_PATH).read(),
            alipay_public_key_string=open(settings.ALIPAY_PUBLIC_KEY_PATH).read(),
            sign_type="RSA2",
            debug=settings.ALIPAY_DEBUG,
        )
        print("创建订单")

        order_string = alipay.client_api(
            "alipay.trade.page.pay",
            biz_content={
                "subject": "充值",
                "out_trade_no": recharge_order.RW_Order_id,
                "total_amount": str(amount),
                "product_code": "FAST_INSTANT_TRADE_PAY",
            },
            return_url=settings.ALIPAY_RETURN_URL,
        )

        # 拼接支付URL
        pay_url = 'https://openapi-sandbox.dl.alipaydev.com/gateway.do?' + order_string
        # 返回支付URL给前端
        return Response({'pay_url': pay_url}, status=status.HTTP_200_OK)
    except Exception as e:
        print("发生异常:")
        print(traceback.format_exc())
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# 提现
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def withdraw(request):
    amount = request.data.get('amount')
    user = request.user

    try:
        if user.account_balance < amount:
            return Response({'error': 'Insufficient balance.'}, status=status.HTTP_400_BAD_REQUEST)
        user.account_balance -= amount
        user.save()
        return Response({'message': f'Withdrawn {amount} successfully.'}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def pay_resault(request):
    order_id =  request.GET.get('out_trade_no')
    amount = request.GET.get('total_amount')
    try:
        print("支付完成 开始处理订单")
        order = RW_Order.objects.get(pk = order_id)
        print(order)
        order.is_paid = True
        user = order.user
        print(user)
        user.account_balance += Decimal(amount)
        user.save()
        print("user保存完成")
        order.save()
        print("order保存完成")
        return JsonResponse({'message': f'Withdrawn {amount} successfully.', 'close_page': True})
    except Exception as e:
        print(e)
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    