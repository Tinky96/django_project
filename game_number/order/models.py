from django.db import models
from goods.models import Product
from user.models import User
# Create your models here.
class orders(models.Model):  
    order_id = models.AutoField(primary_key=True)
    upper = models.ForeignKey(User, on_delete=models.CASCADE,related_name='upper_orders')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='buyer_orders')
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):  
        return str(self.order_id)

class RW_Order(models.Model):
    RW_Order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_recharge = models.BooleanField(default=True)
    user_account = models.CharField(max_length=20, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    
    def __str__(self):  
        return str(self.RW_Order_id)