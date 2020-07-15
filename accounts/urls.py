
from django.urls import path
from .views import  create_book_with_authors

from .views import InstructorRegisterView, LogInView, LogoutView, StudentRegisterView, create_course_with_lessons


app_name = "accounts"

urlpatterns = [
    
    path('create/', create_course_with_lessons),
    path('login/', LogInView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('student/register/', StudentRegisterView.as_view(), name="student-register"),
    path('instructor/register/', InstructorRegisterView.as_view(), name="instructor-register"),
 
    
]
