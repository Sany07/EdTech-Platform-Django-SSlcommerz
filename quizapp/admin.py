from django.contrib import admin
from .models import Quiz, QuizQuestion, QuizExam
# Register your models here.


admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizExam)