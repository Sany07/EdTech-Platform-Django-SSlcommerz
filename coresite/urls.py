
from django.urls import path
from .views import  HomeView, AboutView, search



app_name = "coresite"


urlpatterns = [

    
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('search/', search, name='searchrs'),



]