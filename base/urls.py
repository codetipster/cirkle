
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #pointing django to our application urls in api
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
