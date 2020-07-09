from django.contrib.auth.models import AbstractUser
from django.db import models


from accounts.manager import CustomUserManager
# Create your models here.

Role = (
    ('stu', "Student"),
    ('tea', "Teacher"),
)



class CustomUser(AbstractUser):

    email = models.EmailField(unique=True, blank=False,max_length=254,
                    error_messages={
                        'unique': "A user with that email already exists."
                    })

    role  = models.CharField(max_length=3,choices=Role)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()