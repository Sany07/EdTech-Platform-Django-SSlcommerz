from django.contrib import admin
from .models import Billing, Transaction
# Register your models here.


admin.site.register(Billing),
admin.site.register(Transaction)