

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import CustomUser

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email','username','first_name', 'last_name',  'password1', 'password2',]


class StudentChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email','username','first_name', 'last_name',  'password']