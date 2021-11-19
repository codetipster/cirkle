
from django.urls import path, include
from . import views
from .views import ContactViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers


router = routers.DefaultRouter()
router.register('contacts', ContactViewSet)
# router.register('auth/', obtain_auth_token)

urlpatterns = [
    #pointing our app to a view as defined in views.py
    path('', include(router.urls)),
    # path('test/', Hello.as_view())
    # path('auth/', obtain_auth_token)
]
