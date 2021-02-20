
from django.urls import path
from .views import  CheckoutSuccessView, CheckoutFaildView, InvoiceView



app_name = "billing"


urlpatterns = [

    
    path('success/', CheckoutSuccessView.as_view(), name='success'),
    path('invoice/<slug:tran_id>', InvoiceView.as_view(), name='invoice'),
    path('faild/', CheckoutFaildView.as_view(), name='faild'),

]