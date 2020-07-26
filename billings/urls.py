
from django.urls import path
from .views import  CheckoutSuccessView, CheckoutFaildView



app_name = "billing"


urlpatterns = [

    
    path('success/', CheckoutSuccessView.as_view(), name='success'),
    path('faild/', CheckoutFaildView.as_view(), name='faild'),

]