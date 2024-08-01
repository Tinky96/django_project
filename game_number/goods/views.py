
from rest_framework import generics, viewsets  
from rest_framework.response import Response  
from .models import Category, Product, ProductImage ,Cart
from order.models import orders
from .serializers import CategorySerializer, ProductSerializer,index_ProductSerializer,buy_ProductSerializer,self_ProductSeriliazer,self_ProductBuyerSeriliazer,CartSerializer,platform_info
import os  
from rest_framework.decorators import api_view ,authentication_classes
from user.models import User
from django.conf import settings
from rest_framework.authentication import TokenAuthentication 
from django.db.models import F,Count
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import base64
from django.http import JsonResponse

class CategoryViewSet(viewsets.ModelViewSet):  
    queryset = Category.objects.all()  
    serializer_class = CategorySerializer  
  
class ProductViewSet(viewsets.ModelViewSet):  
    queryset = Product.objects.all()  
    serializer_class = ProductSerializer 


 # 上传
from django.db.models import F

@api_view(['POST'])  
@authentication_classes([TokenAuthentication])  
def create_product(request):  
    user = request.user  
    print(request.META.get('HTTP_AUTHORIZATION')) 
    category_id = request.POST.get('category_id')  
    try:    
        category = Category.objects.get(category_id=category_id)    
    except Category.DoesNotExist:    
        return Response("Invalid category_id", status=400)   
      
    product = Product(  
        user_id=user,  
        product_name=request.POST.get('product_name'),  
        product_number=request.POST.get('product_number'),  
        product_key=request.POST.get('product_key'),  
        product_description=request.POST.get('product_description'),  
        product_price=request.POST.get('product_price'),  
        category_id=category  
    )  
    product.save()  

    # 增加用户的upload_quantity字段值
    user.uploaded_quantity = F('uploaded_quantity') + 1
    user.save(update_fields=['uploaded_quantity'])
  
    product_id = product.product_id  
  
    # 生成新的image路径  
    images = request.FILES.getlist('images')  
    # 重命名并保存图片  
    for i, image_file in enumerate(images):  
        file_extension = os.path.splitext(image_file.name)[1]  # 获取文件扩展名  
        new_filename = f"{product_id}_{i}{file_extension}"  # 假设 product.id 是产品ID的整数值  
        new_file_path = os.path.join(settings.MEDIA_ROOT, 'images', new_filename)  
        with open(new_file_path, 'wb+') as destination:  
            for chunk in image_file.chunks():  
                destination.write(chunk)  
  
        image = ProductImage(  
            product=product,  
            image="images/" + new_filename  
        )  
        image.save()  
  
    return Response(status=201)





# 获取商品信息
@api_view(['GET'])  
@authentication_classes([TokenAuthentication])  
def get_product(request):  
    query = request.GET.get('q', '')  
    category_id = request.GET.get('category_id', '')  
    user = request.GET.get('user', '')  
    products = Product.objects.filter(is_saled=False,useful = True)  
    
    if query:  
        products = products.filter(product_name__icontains=query)  
      
    if category_id:  
        products = products.filter(category_id=category_id)  
      
    if user:  
        products = products.filter(user_id__username=user)  
    product_data = []  
    for product in products:  
        images = ProductImage.objects.filter(product_id=product.product_id)  
        image_urls =images.first().image 
  
        product_dict = {  
            'Product_id': product.product_id,  
            'Product_price': str(product.product_price),  
            'Product_name': product.product_name,  
            'product_upper': product.user_id.username,  
            'category': product.category_id.category_name,  
            'update': product.created_at,  
            'product_image': image_urls  
        }  
        product_data.append(product_dict)  
  
    serializer = index_ProductSerializer(product_data, many=True)  
    return Response(serializer.data) 


# 购买页面的商品信息
@api_view(['GET']) 
def get_one_product(request):  
    P_id = request.GET.get('product_id')
    product = Product.objects.get(pk = P_id)
  
    product_data = []  

    images = ProductImage.objects.filter(product_id=product.product_id)  
    images_url = []
    for image in images:
        images_url.append(image.image)
    
    product_dict = {  
        'product_id' : product.product_id,
        'Product_price': str(product.product_price),  
        'Product_name': product.product_name,  
        'product_upper': product.user_id.username,  
        'category': product.category_id.category_name, 
        'description': product.product_description, 
        'update': product.created_at,  
        'images': images_url
    }  
    product_data.append(product_dict)  
  
    serializer = buy_ProductSerializer(product_data, many=True)  
    return Response(serializer.data) 


# 搜索
@api_view(['GET'])  
def search_product(request):  
    query = request.GET.get('q', '')  # 获取搜索关键词  
    if query:  
        # 使用icontains进行模糊搜索，这样可以不区分大小写地搜索包含关键词的产品名称  
        products = Product.objects.filter(product_name__icontains=query, is_saled=False)  
    else:  
        products = Product.objects.filter(is_saled=False)  
  
    product_data = []  
    for product in products:  
        images = ProductImage.objects.filter(product=product)  
        image_url = images.first().image 
  
        product_dict = {  
            'Product_id': product.product_id,  
            'Product_price': str(product.product_price),  
            'Product_name': product.product_name,  
            'product_upper': product.user_id.username,  
            'category': product.category_id.category_name,  
            'update': product.created_at,  
            'product_image': image_url
        }  
        product_data.append(product_dict)  
  
    serializer = index_ProductSerializer(product_data, many=True)  
    return Response(serializer.data)  



# 个人页面显示出售的商品信息显示
@api_view(['GET']) 
@authentication_classes([TokenAuthentication])  
def self_products(request):  
    user = request.user
    # user_id = request.GET.get('user')
    # user = User.objects.get(pk = user_id)
    products = Product.objects.filter(user_id = user)
    product_data = []
    for product in products:
        product_dict = {  
            'product_id' : product.product_id,
            'Product_price': str(product.product_price),  
            'Product_name': product.product_name,  
            'category': product.category_id.category_name, 
            'description': product.product_description, 
            'update': product.created_at,  
            'isSaled': product.is_saled
        }  
        product_data.append(product_dict)  
  
    serializer = self_ProductSeriliazer(product_data, many=True)  
    return Response(serializer.data) 

# 个人信息页面显示购买的商品信息
@api_view(['GET']) 
@authentication_classes([TokenAuthentication])  
def buy_products(request):  
    # user = request.user
    user_id = request.GET.get('user')
    user = User.objects.get(pk = user_id)
    Orders = orders.objects.filter(buyer = user)
    product_data = []
    print(Orders)
    for order in Orders:
        product = order.Product
        product_dict = {  
            'product_id' : product.product_id,
            'Product_price': str(product.product_price),  
            'Product_name': product.product_name,  
            'category': product.category_id.category_name, 
            'description': product.product_description, 
            'product_number': product.product_number,  
            'product_key': product.product_key,
            'order_id' : order.order_id,
        }  
        product_data.append(product_dict)  
  
    serializer = self_ProductBuyerSeriliazer(product_data, many=True)  
    return Response(serializer.data) 


# 修改
@api_view(['PUT'])  
@authentication_classes([TokenAuthentication])  
def update_product(request, product_id):  
    try:  
        product = Product.objects.get(product_id=product_id)  
    except Product.DoesNotExist:  
        return Response("Invalid product_id", status=400)  
  
    # 检查是否有权限修改该商品，例如只允许商品的创建者修改  
    if product.user_id != request.user:  
        return Response("You are not authorized to update this product", status=403)  
  
    # 更新商品的字段  
    product.product_name = request.data.get('product_name', product.product_name)  
    product.product_number = request.data.get('product_number', product.product_number)  
    product.product_key = request.data.get('product_key', product.product_key)  
    product.product_description = request.data.get('product_description', product.product_description)  
    product.product_price = request.data.get('product_price', product.product_price)  
  
    # 保存更新后的商品对象  
    product.save()  
  
    # 删除原先关联的商品图片记录和文件  
    for image in product.productimage_set.all():  
        # 删除记录  
        image.delete()  
        # 删除文件  
        image_path = os.path.join(settings.MEDIA_ROOT, image.image.name)  
        if os.path.exists(image_path):  
            os.remove(image_path)  
  
    # 处理新上传的商品图片  
    images = request.FILES.getlist('images')  
    for i, image_file in enumerate(images):  
        # 保存文件  
        file_extension = os.path.splitext(image_file.name)[1]  # 获取文件扩展名  
        new_filename = f"{product_id}_{i}{file_extension}"  # 假设 product.id 是产品ID的整数值  
        new_file_path = os.path.join(settings.MEDIA_ROOT, 'images', new_filename)  
        with open(new_file_path, 'wb+') as destination:  
            for chunk in image_file.chunks():  
                destination.write(chunk)  
  
        # 创建新的商品图片记录  
        image = ProductImage(  
            product=product,  
            image="images/" + new_filename  
        )  
        image.save()  
  
    return Response(status=200)  


# 上传至
@api_view(['POST'])  
def add_to_cart(request):  
    user_id = request.data.get('user_id')  
    product_id = request.data.get('product_id')  
  
    # 检查用户是否已经添加过相同的商品到购物车  
    try:  
        existing_cart = Cart.objects.get(user_id=user_id, product_id=product_id)  
        return Response({'message': '该商品已经添加到购物车！'}, status=400)  
    except Cart.DoesNotExist:  
        pass  
  
    serializer = CartSerializer(data=request.data)  
    if serializer.is_valid():  
        serializer.save()  
        return Response(serializer.data, status=201)  
    return Response(serializer.errors, status=400) 
 
# 移除购物车
@api_view(['DELETE'])  
def remove_from_cart(request):
    print(request.data)
    user_id = request.data.get('user_id')  # 修改为正确的参数名
    product_id = request.data.get('product_id')  # 修改为正确的参数名
    print(product_id)
    try:  
        user = User.objects.get(pk=user_id)  # 使用实际的 User 对象
        product = Product.objects.get(pk=product_id)  # 使用实际的 Product 对象
        cart = Cart.objects.get(user_id=user, product_id=product)  # 使用实际的 User 和 Product 对象来过滤购物车
        cart.delete()
        return Response(status=204)  
    except Cart.DoesNotExist:  
        return Response(status=404)
 
  


# 获取购物车
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_carts(request):
    user_id = request.GET.get('user')
    user = User.objects.get(pk=user_id)
    carts = Cart.objects.filter(user_id=user)

    product_data = []
    for cart in carts:
        product = cart.product_id
        if not product.is_saled:  # 只获取 is_saled 字段为 False 的产品
            images = ProductImage.objects.filter(product=product)
            image_url = images.first().image
            product_dict = {
                'Product_id': product.product_id,
                'Product_price': str(product.product_price),
                'Product_name': product.product_name,
                'product_upper': product.user_id.username,
                'category': product.category_id.category_name,
                'update': product.created_at,
                'product_image': image_url
            }
            product_data.append(product_dict)

    serializer = index_ProductSerializer(product_data, many=True)
    return Response(serializer.data)


# 获取图表
def fetch_data():
    # 获取订单数据
    orders_data = orders.objects.all().values('date', 'Product__product_name', 'buyer_id', 'upper_id', 'Product__category_id')
    df_orders = pd.DataFrame(orders_data)

    # 获取商品数据
    product_data = Product.objects.all().values('product_name', 'category_id', 'is_saled')
    df_products = pd.DataFrame(product_data)

    # 获取类别数据
    category_data = Category.objects.all().values('category_id', 'category_name')
    df_categories = pd.DataFrame(category_data)

    return df_orders, df_products, df_categories

def process_data(df_orders, df_products, df_categories):
    # 将日期字段转换为datetime类型
    df_orders['date'] = pd.to_datetime(df_orders['date'])

    # 销售趋势：按日期分组
    trend_data = df_orders.groupby(df_orders['date'].dt.to_period('M')).size().reset_index(name='count')
    trend_data['date'] = trend_data['date'].dt.to_timestamp()

    # 售出商品类别分布
    sold_category_dist = df_orders['Product__category_id'].value_counts().reset_index()
    sold_category_dist.columns = ['category_id', 'count']
    sold_category_dist = sold_category_dist.merge(df_categories, on='category_id')

    # 正在售卖商品类别分布
    on_sale_products = df_products[df_products['is_saled'] == False]
    on_sale_category_dist = on_sale_products['category_id'].value_counts().reset_index()
    on_sale_category_dist.columns = ['category_id', 'count']
    on_sale_category_dist = on_sale_category_dist.merge(df_categories, on='category_id')

    return trend_data, sold_category_dist, on_sale_category_dist

def plot_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    return img_base64

@api_view(['GET'])
def get_images(request):
    # 获取并处理数据
    df_orders, df_products, df_categories = fetch_data()
    trend_data, sold_category_dist, on_sale_category_dist = process_data(df_orders, df_products, df_categories)
    
    # 绘制销售趋势图
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(trend_data['date'], trend_data['count'])
    ax.set_title('销售趋势')
    ax.set_xlabel('日期')
    ax.set_ylabel('交易数量')
    trend_img_base64 = plot_to_base64(fig)
    plt.close(fig)

    # 绘制售出商品类别分布图
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(sold_category_dist['count'], labels=sold_category_dist['category_name'], autopct='%1.1f%%', startangle=90)
    ax.set_title('售出商品类别分布')
    sold_category_img_base64 = plot_to_base64(fig)
    plt.close(fig)

    # 绘制正在售卖商品类别分布图
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(on_sale_category_dist['count'], labels=on_sale_category_dist['category_name'], autopct='%1.1f%%', startangle=90)
    ax.set_title('正在售卖商品类别分布')
    on_sale_category_img_base64 = plot_to_base64(fig)
    plt.close(fig)

    # 将图表数据打包成JSON格式
    data = {
        'trend_image': trend_img_base64,
        'sold_category_image': sold_category_img_base64,
        'on_sale_category_image': on_sale_category_img_base64
    }
    
    return JsonResponse(data)