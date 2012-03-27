#coding: utf-8

# primeiro importa coisas do python, segundo do django e terceiro da aplicacao
from django.contrib import admin
from .models import Cliente

admin.site.register(Cliente)
