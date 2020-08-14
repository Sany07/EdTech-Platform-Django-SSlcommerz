from django.urls import path

from .views import DashBoardView, \
TotalUsersView, TotalInstructorsView, TotalStudentsView, CoursesView, NewCoursesView, CourseDetailView


app_name = "customadmin"

urlpatterns = [

    
    path('dashboard/', DashBoardView.as_view(), name="dashboard"),
    path('users/', TotalUsersView.as_view(), name="users"),
    path('instructors/', TotalInstructorsView.as_view(), name="instructors"),
    path('students/', TotalStudentsView.as_view(), name="students"),
    path('courses/', CoursesView.as_view(), name="courses"),
    path('new-courses/', NewCoursesView.as_view(), name="new-courses"),
    path('course/<slug:slug>/', CourseDetailView.as_view(), name="single-course"),


]
