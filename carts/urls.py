
from django.urls import path
from .views import  CartView, CheckoutView, cart_home, cart_update



app_name = "cart"


urlpatterns = [

    
    path('', cart_home, name='cart'),
    path('checkout/<int:id>', CheckoutView.as_view(), name='checkout'),
    path('update/', cart_update, name='cart-update'),

]