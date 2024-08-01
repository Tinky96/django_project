from rest_framework import serializers
from .models import orders,RW_Order
from goods.models import Product

    
  
class OrderSerializer(serializers.ModelSerializer):  
    product_id = serializers.PrimaryKeyRelatedField(  
        queryset=Product.objects.all(),  
        write_only=True,  
        source='Product'  
    )  
  
    class Meta:  
        model = orders  
        fields = ['buyer', 'upper', 'product_id']  # 从列表中省略了'id'  
        # 如果你希望在序列化时包含Product的详细信息，可以添加如下行：  
        # read_only_fields = ['product']  
  
    def create(self, validated_data):  
        # 使用validated_data创建Order实例  
        return orders.objects.create(**validated_data) 

class RW_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RW_Order
        fields = '__all__'