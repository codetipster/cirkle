# from django.http.response import HttpResponse
# from django.shortcuts import render
# from django.views import View

# from django.db.models.query import QuerySet
from api.serializer import ContactSerializer
from .models import Contact
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ContactViewSet(viewsets.ModelViewSet):
    """Creating a DRF based view with viewsets from serializer"""
    queryset = Contact.objects.all().order_by('name')
    serializer_class = ContactSerializer

    





















# def welcome(request):
#     """ A function based view without DRF"""
#     return HttpResponse('Welcome to our first views from django without DRF')


# class Hello(View):
#     """ A class based view without DRF"""
#     #get all the contact in database
#     contacts = Contact.objects.all()
#     # contacts = Contact.objects.filter(property=True)=> returns all contact meeting criterion
#     # contacts = Contact.objects.get()=> returns only one contact with an attribute 
#     #loop through the array of contacts
#     for contact in contacts:
#         message = f"You have {contact.name} in your Cirkle"
    

#     def get(self, request):
        
#         return HttpResponse(self.message)


    # #what serializer should the viewset use?
    # serializer_class = ContactSerializer
    # #define the queryset
    # queryset = Contact.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)