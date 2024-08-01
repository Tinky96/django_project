from django.urls import include, path  
from rest_framework import routers  
from .views import CategoryViewSet, create_product,ProductViewSet,get_product,get_one_product,search_product,self_products,buy_products,update_product,add_to_cart,remove_from_cart,get_carts,get_images
router = routers.DefaultRouter()  
router.register(r'categories', CategoryViewSet)  
router.register(r'products', ProductViewSet)  
# router.register(r'product-images', ProductImageViewSet)    


urlpatterns = [  
    path('', include(router.urls)),  
    path('create_product/', create_product, name='create_product'),
    path('get_product/', get_product, name='get_all_product'),  
    path('get_one_product/', get_one_product, name='get_one_product'),
    path('search/', search_product, name='search_product'),  
    path('self_products/', self_products, name='self_products'), 
    path('buy_products/', buy_products, name='buy_products'), 
    path('update_products/', update_product, name='update_products'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/', remove_from_cart, name='remove_from_cart'),
    path('get_carts/', get_carts, name='get_carts'),
    path('get_images/', get_images, name='get_images'),
]  

