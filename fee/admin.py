from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import  FEES, FeeUpdate, FeeSem, Payments

admin.site.register(FEES)
admin.site.register(FeeUpdate)
admin.site.register(FeeSem)
admin.site.register(Payments)