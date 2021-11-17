from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Contact

# Create your views here.

def welcome(request):
    """ A function based view"""
    return HttpResponse('Welcome to our first views from django without DRF')


class Hello(View):
    """ A class based view without DRF"""
    #get all the contact in database
    contacts = Contact.objects.all()
    # contacts = Contact.objects.filter(property=True)=> returns all contact meeting criterion
    # contacts = Contact.objects.get()=> returns only one contact with an attribute 
    #loop through the array of contacts
    for contact in contacts:
        message = f"You have {contact.name} in your Cirkle"
    

    def get(self, request):
        
        return HttpResponse(self.message)