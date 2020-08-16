from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(FrontEndSettings)
admin.site.register(StaticFileSettings)
admin.site.register(PaymentGatewaySettings)