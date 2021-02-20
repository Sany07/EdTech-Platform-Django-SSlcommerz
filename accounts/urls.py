
from django.urls import path, include


from .views import InstructorRegisterView, ProfileView, LogInView, LogoutView, StudentRegisterView,EditProfileView, SettingView , ChangePassword


app_name = "accounts"

urlpatterns = [
    
    path('login/', LogInView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/<int:id>/', ProfileView.as_view(), name="profile"),
    path('student/register/', StudentRegisterView.as_view(), name="student-register"),
    path('instructor/register/', InstructorRegisterView.as_view(), name="instructor-register"),
    path('settings/', SettingView.as_view() ,name="setting"),
    path('profile/update/',EditProfileView ,name="profile-update"),
    path('password/', ChangePassword, name='change_password'),

    
 
    
]

