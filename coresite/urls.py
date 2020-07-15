
from django.urls import path
from .views import  HomeView



app_name = "coresite"


urlpatterns = [

    
    path('', HomeView.as_view(), name='home'),



]