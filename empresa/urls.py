from django.contrib import admin
from django.urls import path
from .views import *
app_name='empresa'
urlpatterns = [
    path('cadastro-empresa',template_cad,name='empresa_cad'),
    
    ]