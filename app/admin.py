from django.contrib import admin
from app import models


class AddressAdmin(admin.ModelAdmin):
    ''' Admin layout for Address'''
    pass

# Register Admin layouts into django
admin.site.register(models.Address, AddressAdmin)
