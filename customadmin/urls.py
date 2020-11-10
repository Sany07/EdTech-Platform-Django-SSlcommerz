from django.urls import include, path

from .views import *


app_name = "customadmin"

urlpatterns = [

    
    path('', DashBoardView.as_view(), name="dashboard"),
    path('users/', AllUsersView.as_view(), name="users"),
    path('instructors/', TotalInstructorsView.as_view(), name="instructors"),
    path('students/', TotalStudentsView.as_view(), name="students"),
    path('courses/', CoursesView.as_view(), name="courses"),
    path('new-courses/', NewCoursesView.as_view(), name="new-courses"),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name="single-course"),
    path('approvedorreject/', approvedOrReject, name="approvedorreject"),
    path('settings/gateway/update',  PaymentGatewaySettingsView.as_view(), name="gateway-settings"),

    path('settings/', include([
            path('frontend/update', FrontEndSettings.as_view(), name="frontend-settings"),
    ])),


]
