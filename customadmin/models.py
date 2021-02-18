from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

CURRENCY_CHOICES =( 

    ("TK", "TK(BDT)"), 
    ("$", "$(USA)"), 

) 

class FrontEndSettings(models.Model):
    logo =models.ImageField(upload_to='photos/frontend/logo/', blank=True, null=True)
    text_logo = models.CharField(blank=True, null=True, max_length=20)
    is_teacher_register = models.BooleanField(default=True)
    currency = models.CharField(max_length=2,choices = CURRENCY_CHOICES, default='TK') 
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



class About(models.Model):
    title = models.CharField(max_length=250,blank=False)
    description = RichTextField()
    our_mission = RichTextField()
    who_we_are = RichTextField()
    thumbnail_one = models.ImageField(upload_to='photos/about/%Y-%m-%d/')
    thumbnail_two = models.ImageField(upload_to='photos/about/%Y-%m-%d/')
    thumbnail_three = models.ImageField(upload_to='photos/about/%Y-%m-%d/')


    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
        db_table = "about"

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=250,blank=False)
    testimonial = models.TextField()


    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        db_table = "testimonial"

    def __str__(self):
        return self.testimonial