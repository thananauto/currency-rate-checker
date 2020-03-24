from django.contrib import admin
from . models import Currency

# Register your models here.

class CurrencyAdmin(admin.ModelAdmin):
    fields = ['cur'] 

admin.site.register(Currency, CurrencyAdmin)