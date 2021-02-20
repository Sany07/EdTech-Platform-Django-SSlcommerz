from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed


from courses.models import Course


User = settings.AUTH_USER_MODEL
# Create your models here.
class InstractorPayment(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    total       = models.DecimalField(default=0.00, max_digits=65, decimal_places=2)


    def __str__(self):
        return str(self.id)


# def pre_save_instractorpayment_receiver(sender, instance, *args, **kwargs):
#     if instance.total > 0:
#         instance.total = Decimal(instance.total) #* Decimal(1) # 8% tax
#     else:
#         instance.total = 0.00
# pre_save.connect(pre_save_instractorpayment_receiver, sender=InstractorPayment)