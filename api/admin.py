from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from . import models

# Register your models here.
admin.site.register(models.UserProfile)  #generic registration

#customize the registration
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Customizes the admin view for our contact object fields"""
    # fieds = ["add fields"]
    list_display = ['name', 'phone_number', 'email']
    list_filter = ['created_on']
    search_fields = ['name', ]

