from django.urls import include, path
from django.views.generic import RedirectView

from .views import *


app_name = "customadmin"

urlpatterns = [

    
    path('', RedirectView.as_view(url='dashboard/')),
    path('dashboard/', DashBoardView.as_view(), name="dashboard"),
    path('users/', AllUsersView.as_view(), name="users"),
    path('instructors/', AllInstructorsView.as_view(), name="instructors"),
    path('students/', AllStudentsView.as_view(), name="students"),
    path('courses/', CoursesView.as_view(), name="courses"),
    path('profile/<int:pk>', ProfileView.as_view(), name="profile"),
    path('courses/', CoursesView.as_view(), name="all-courses"),
    path('newcourses/', NewCoursesView.as_view(), name="new-courses"),  
    path('categories/', CategoryView.as_view(), name="categories"),
    path('create/category/', CreateCategoryView.as_view(), name="new-category"),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name="single-course"),
    path('approvedorreject/', approvedOrReject, name="approvedorreject"),

    path('settings/', include([
            path('gateway/update',  PaymentGatewaySettingsView.as_view(), name="gateway-settings"),
            path('general/update', FrontEndSettings.as_view(), name="frontend-settings"),
    ])),


]
