
from django.urls import path
from .views import  CheckoutSuccessView



app_name = "cart"


urlpatterns = [

    
    path('success/', CheckoutSuccessView.as_view(), name='success'),

]