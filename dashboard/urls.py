
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import MyCourseListView, StartCourseView



app_name = "dashboard"

urlpatterns = [
    path('my-courses/', MyCourseListView.as_view(), name="my-courses"),
    # path('start/<int:id>/', courseview, name="start-course"),
    path('start-course/<slug:slug>/', StartCourseView.as_view(), name="start-course"),
]

