
from django.urls import path
from . import views

urlpatterns = [
    #pointing our app to a view as defined in views.py
    path('', views.welcome),
]
