from django.db import models
from user.models import User


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_number = models.CharField(max_length=20)
    product_key = models.CharField(max_length=20)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    is_saled = models.BooleanField(default=False)
    useful = models.BooleanField(default=True)  

    def __str__(self):
        return self.product_name



class ProductImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", default="default_image.jpg")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url

#购物车
class Cart(models.Model):  
    cart_id = models.AutoField(primary_key=True)  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)  
  
    def __str__(self):  
       return str(self.cart_id)
