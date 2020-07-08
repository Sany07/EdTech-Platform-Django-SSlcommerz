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
    ('student', "Student"),
    ('teacher', "Teacher"),
)



class CustomUser(AbstractUser):
    # pass

    email = models.EmailField(unique=True, blank=False,
                    error_messages={
                        'unique': "A user with that email already exists."
                    })

    role  = models.ChoiceField(choice=Role,max_length=10)

    # objects = CustomUserManager()