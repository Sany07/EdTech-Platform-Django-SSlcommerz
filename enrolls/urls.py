
from django.urls import include, path
from .views import EnrollView


app_name = "enrollment"
urlpatterns = [
    path('enroll/', EnrollView.as_view(), name="enroll"),

]

