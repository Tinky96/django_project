from rest_framework import serializers  
from .models import Category, Product, ProductImage ,Cart
from user.models import User
class CategorySerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Category  
        fields = '__all__'  
  
class ProductImageSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = ProductImage  
        fields = '__all__'
  
class ProductSerializer(serializers.Serializer):  
    user_id = serializers.CharField(max_length=20) 
    product_name = serializers.CharField(max_length=100)  
    product_number = serializers.CharField(max_length=20)  
    product_key = serializers.CharField(max_length=20)  
    product_description = serializers.CharField(max_length=100)  
    product_price = serializers.DecimalField(max_digits=8, decimal_places=2)
    category_id = serializers.IntegerField()  
     
    images = serializers.ListField(child=serializers.FileField())  
    
    def create(self, validated_data):  
        # 在这里可以执行保存数据的逻辑，或者将数据传递给视图进行处理  
        return validated_data  
  
    def update(self, instance, validated_data):  
        # 在这里可以执行更新数据的逻辑，或者将数据传递给视图进行处理  
        return validated_data

class index_ProductSerializer(serializers.Serializer):
    Product_id = serializers.CharField(max_length = 100)
    Product_name = serializers.CharField(max_length = 100)
    Product_price = serializers.DecimalField(max_digits=8,decimal_places=2)
    product_image = serializers.ImageField()
    product_upper = serializers.CharField(max_length = 20)
    category = serializers.CharField(max_length = 10)
    update = serializers.DateField()

class buy_ProductSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length = 100)
    Product_name = serializers.CharField(max_length = 100)
    Product_price = serializers.DecimalField(max_digits=8,decimal_places=2)
    product_upper = serializers.CharField(max_length = 20)
    description = serializers.CharField(max_length = 100)
    update = serializers.DateField()
    category = serializers.CharField(max_length = 10)
    images = serializers.ListField(child=serializers.FileField())
        
# 个人信息页面 获取个人上传的页面
class self_ProductSeriliazer(serializers.Serializer):
    product_id = serializers.CharField(max_length = 100)
    Product_price = serializers.DecimalField(max_digits=8,decimal_places=2)
    Product_name = serializers.CharField(max_length = 100)
    category = serializers.CharField(max_length = 100)
    description = serializers.CharField(max_length = 100)
    update = serializers.DateField()
    isSaled = serializers.BooleanField()


# 个人信息页面获取个人购买的页面
class self_ProductBuyerSeriliazer(serializers.Serializer):
    product_id = serializers.CharField(max_length = 100)
    Product_price = serializers.DecimalField(max_digits=8,decimal_places=2)
    Product_name = serializers.CharField(max_length = 100)
    category = serializers.CharField(max_length = 100)
    description = serializers.CharField(max_length = 100)
    product_number = serializers.CharField(max_length = 100)
    product_key = serializers.CharField(max_length = 100)


class CartSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Cart  
        fields = ['cart_id', 'user_id', 'product_id', 'created_at']  
        
        
        
class platform_info(serializers.Serializer):
    info_image = serializers.ImageField()
    Product_count = serializers.IntegerField()
    order_count = serializers.IntegerField()
