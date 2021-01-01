from django.contrib import admin

# Register your models here.
from .models import Contactcomplain, Contactenquiry
admin.site.register(Contactcomplain)
admin.site.register(Contactenquiry)