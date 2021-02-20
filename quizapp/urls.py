
from django.contrib import admin
from django.urls import include, path
from .views import AddQuiz, AddQuizQuestion, Exam, save_ans ,result,clr, certificate

app_name = "quiz"
urlpatterns = [
    path('add/<int:id>/', AddQuiz, name="add_quiz"),
    path('add/question/<int:id>/', AddQuizQuestion, name="add_quiz_question"),
    path('course/quiz/<int:id>/', Exam, name="exam"),
    path('save_ans/', save_ans, name="save_ans"),
    path('result/<int:id>/', result, name="quiz_result"),
    path('certificate/<int:id>/', certificate, name="certificate"),
    # path('result/', result, name="quiz_result"),
    path('clr/', clr, name="clr"),

]