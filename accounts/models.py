from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from accounts.manager import CustomUserManager
# Create your models here.

from django.conf import settings
User= settings.AUTH_USER_MODEL


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


class Profile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    designation = models.CharField(max_length=100,blank=True)
    website = models.URLField( blank=True)
    profile_pic =models.ImageField(upload_to='photos/profile/%Y-%m-%d/')


    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        db_table = "profiles"

    def __str__(self):
        return self.user_profile.username

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={'id': self.id})



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_profile=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()