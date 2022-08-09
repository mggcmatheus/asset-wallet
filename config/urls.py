from django.contrib import admin
from django.urls import path
from app.api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', api.urls)
]
