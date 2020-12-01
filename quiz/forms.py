from django import forms
from django.forms import modelformset_factory

from .models import *

class BookModelForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ('choice_one', )
        labels = {
            'choice_one': 'Book Name'
        }
        widgets = {
            'choice_one': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Book Name here'
                }
            )
        }
