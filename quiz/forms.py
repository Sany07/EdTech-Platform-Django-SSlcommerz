from django import forms
from django.forms import modelformset_factory

from .models import *

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        exclude = '__all__'

class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        exclude = ['quiz']