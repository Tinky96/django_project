from django.urls import path  
from . import views  
  
urlpatterns = [  
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),  
    path('self_message/', views.get_user_info, name='get_user_info'),  
    path('recharge/', views.recharge, name='get_user_info'),
    path('withdraw/', views.withdraw, name='get_user_info'),
    path('pay_resault/',views.pay_resault,name = 'pay_resaul'),
    # 这里可以添加其他URL模式  
]