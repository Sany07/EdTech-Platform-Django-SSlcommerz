from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

from courses.models import Course

class Billing(models.Model):
    user        = models.ForeignKey(User, on_delete=models.DO_NOTHING)
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


class Transaction(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # biling_profile = models.ForeignKey(Billing, on_delete=models.DO_NOTHING)
    # products    = models.ManyToManyField(Course, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    tran_id = models.CharField(max_length=15)
    val_id = models.CharField(max_length=75)
    card_type = models.CharField(max_length=150)
    store_amount = models.DecimalField(max_digits=10, decimal_places=2)
    card_no = models.CharField(max_length=55, null=True)
    bank_tran_id = models.CharField(max_length=155, null=True)
    status = models.CharField(max_length=55)
    tran_date = models.DateTimeField()
    currency = models.CharField(max_length=10)
    card_issuer = models.CharField(max_length=255)
    card_brand = models.CharField(max_length=15)
    card_issuer_country = models.CharField(max_length=55)
    card_issuer_country_code = models.CharField(max_length=55)
    currency_rate = models.DecimalField(max_digits=10, decimal_places=2)
    verify_sign = models.CharField(max_length=155)
    verify_sign_sha2 = models.CharField(max_length=255)
    risk_level = models.CharField(max_length=15)
    risk_title = models.CharField(max_length=25)


    def __str__(self):
        return self.user.username