
from django.urls import path
from .views import  create_book_with_authors

from .views import create_book_with_authors


app_name = "courses"

urlpatterns = [
    
    path('create/', create_book_with_authors),
 
    
]
