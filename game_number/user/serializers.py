from rest_framework import serializers  
from .models import User  
  
class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['username', 'password', 'email']  
        extra_kwargs = {  
            'password': {'write_only': True},  
        }  
  
    def create(self, validated_data):  
        user = User.objects.create(**validated_data)  
        user.set_password(validated_data['password'])  
        user.save()  
        return user
    
class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'created_at', 'uploaded_quantity', 'purchased_quantity', 'sold_quantity', 'account_balance']
