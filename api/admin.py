from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Contact

# Register your models here.
# admin.site.register(Contact)  #generic registration

#customize the registration
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Customizes the admin view for our contact object fields"""
    # fieds = ["add fields"]
    list_display = ['name', 'phone_number', 'email']
    list_filter = ['created_on']
    search_fields = ['name', ]

