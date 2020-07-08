from django.contrib.auth.models import AbstractUser
from django.db import models


from accounts.manager import CustomUserManager
# Create your models here.

"""

# Tutorial
    - name
    - price
    - description
    - thumbnail
    - demo - url -
    - category [ foreign key ]
    - lessons [ many to many ]

# lessons
    - name
    - videos -1
    - videos -2
    - videos -3


"""
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
    REQUIRED_FIELDS = []

    objects = CustomUserManager()