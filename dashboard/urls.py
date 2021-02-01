
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import DashboardView, MyEnrolledCourseListView, StartCourseView, InstructorCourseListView



app_name = "dashboard"

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('my-courses/', InstructorCourseListView.as_view(), name="instructor-courses"),
    path('enrolled-courses/', MyEnrolledCourseListView.as_view(), name="my-courses"),
    path('classroom/<slug:slug>/', StartCourseView.as_view(), name="start-course"),
]

