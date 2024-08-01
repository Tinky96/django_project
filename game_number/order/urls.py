from django.urls import path  
from . import views  
  
urlpatterns = [  
    path('make_order/', views.make_order, name='make_order'), 
    path('make_orders/', views.make_orders, name='make_orders'), 
    path('get_rw_orders/', views.get_rw_orders, name='get_rw_orders'), 
    path('withdraw/', views.create_rw_order, name='withdraw'), 

    # 这里可以添加其他URL模式  
]