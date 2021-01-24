from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL
from courses.models import Course

class EnrollCouese(models.Model):

    user        = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    products    = models.ManyToManyField(Course, blank=True, related_name='products')
    timestamp   = models.DateTimeField(auto_now= True, auto_now_add=False)
    #timestamp.editable = True

    class Meta:
        verbose_name = "Enroll"
        verbose_name_plural ="Enrolls"
        db_table = "EnrollCoueses"
        

    def __str__(self):
        return self.user.username

    # def get_absolute_url(self):
    #     return reverse("Enroll_detail", kwargs={"pk": self.pk})
