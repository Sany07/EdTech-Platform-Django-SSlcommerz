
from django.urls import include, path
from .views import QuizAdd


app_name = "quiz"
urlpatterns = [
    path('', QuizAdd, name="quiz"),

]

