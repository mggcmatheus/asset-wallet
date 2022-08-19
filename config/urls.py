from django.contrib import admin
from django.urls import path
from registration.api import api as registration_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', registration_api.urls)
]
