from django.contrib import admin
from .models import Quiz, QuizQuestion, QuizExam, Certificate
# Register your models here.


admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizExam)
admin.site.register(Certificate)