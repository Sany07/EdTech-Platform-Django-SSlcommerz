from django.urls import path

from .views import DashBoardView, TotalUsersView, TotalInstructorsView, TotalStudentsView


app_name = "customadmin"

urlpatterns = [

    
    path('dashboard/', DashBoardView.as_view(), name="dashboard"),
    path('users/', TotalUsersView.as_view(), name="users"),
    path('instructors/', TotalInstructorsView.as_view(), name="instructors"),
    path('students/', TotalStudentsView.as_view(), name="students"),
    # path('totalusers/', TotalUsersView.as_view(), name="totalusers"),



]
