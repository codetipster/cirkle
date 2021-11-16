
from django.urls import path
from . import views
from .views import Hello

urlpatterns = [
    #pointing our app to a view as defined in views.py
    path('', views.welcome),
    path('test/', Hello.as_view())
]
