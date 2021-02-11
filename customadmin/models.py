from django.db import models

# Create your models here.
class FrontEndSettings(models.Model):
    logo =models.ImageField(upload_to='photos/frontend/logo/', blank=True, null=True)
    text_logo = models.CharField(blank=True, null=True, max_length=20)
    is_teacher_register = models.BooleanField(default=True)
    footer = models.CharField(max_length=30)


    class Meta:
        verbose_name = "FrontEndSetting"
        verbose_name_plural = "FrontEndSettings"
        db_table = "frontendsettings"

    def __str__(self):
        return self.footer


class StaticFileSettings(models.Model):
    is_use_aws = models.BooleanField(default=False)
    aws_groupname = models.CharField(max_length=200, blank=True, null=True)
    aws_username = models.CharField(max_length=200, blank=True, null=True)
    aws_access_key_id = models.CharField(max_length=200, blank=True, null=True)
    aws_secret_access_key = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        verbose_name = "StaticFileSetting"
        verbose_name_plural = "StaticFileSettings"
        db_table = "staticfilesettings"


class PaymentGatewaySettings(models.Model):

    store_id = models.CharField(max_length=500, blank=True, null=True)
    store_pass = models.CharField(max_length=500, blank=True, null=True)
    
    class Meta:
        verbose_name = "PaymentGatewaySetting"
        verbose_name_plural = "PaymentGatewaySettings"
        db_table = "paymentgatewaysettings"
