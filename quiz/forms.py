from django import forms
from django.forms import modelformset_factory

from .models import *

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['descriptions']

class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = '__all__'
        