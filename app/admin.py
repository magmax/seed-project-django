from django.contrib import admin
from app.models import *


class AddressAdmin(admin.ModelAdmin):
    ''' Admin layout for Address'''
    pass

''' Register Admin layouts into django'''
admin.site.register(Address, AddressAdmin)
