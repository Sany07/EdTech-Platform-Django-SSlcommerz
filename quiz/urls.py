
from django.urls import include, path
from .views import AddQuiz, AddQuizQuestion


app_name = "quiz"
urlpatterns = [
    path('', AddQuiz, name="add_quiz"),
    path('add/question/<int:id>/', AddQuizQuestion, name="add_quiz_question"),

]

