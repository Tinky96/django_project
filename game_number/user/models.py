from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, email=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, email=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, password, email, **extra_fields)


class User(AbstractUser):
    username = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_quantity = models.IntegerField(default=0)  # 上传数量
    purchased_quantity = models.IntegerField(default=0)  # 购买数量
    sold_quantity = models.IntegerField(default=0)  # 已售商品数量
    account_balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )  # 账户余额

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
