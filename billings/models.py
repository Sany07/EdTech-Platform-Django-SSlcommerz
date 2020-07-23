from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Billing(models.Model):
    user        = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # products    = models.ManyToManyField(Course, blank=True)
    full_name   = models.CharField(max_length=50)
    email       = models.EmailField(max_length=50)
    phone       = models.CharField(max_length=13)
    address     = models.CharField(max_length=50)
    Street_addreess   = models.CharField(max_length=50)
    city        = models.CharField(max_length=50)
    post_code        = models.CharField(max_length=50)
    timestamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Billing"
        verbose_name_plural = "Billings"
        db_table = "billing"

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     return reverse("courses:single-course", kwargs={'slug': self.slug})