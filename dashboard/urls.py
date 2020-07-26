
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import MyCourseListView



app_name = "dashboard"

urlpatterns = [
    path('my-courses/', MyCourseListView.as_view(), name="my-courses"),
]

