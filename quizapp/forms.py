from django import forms

from .models import *

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['descriptions']

class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = '__all__'


class QuizExamForm(forms.ModelForm):
    class Meta:
        model = QuizExam
        fields = '__all__'
        