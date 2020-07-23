
from django.urls import path
from .views import  CartView, cart_home, cart_update, checkout



app_name = "cart"


urlpatterns = [

    
    path('', cart_home, name='cart'),
    path('checkout/<int:id>/', checkout, name='checkout'),
    path('update/', cart_update, name='cart-update'),

]