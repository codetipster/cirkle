from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def welcome(request):
    return HttpResponse('Welcome to our first views from django without DRF')
