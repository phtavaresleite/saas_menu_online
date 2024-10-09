from django.contrib import admin
from django.urls import path, include
from .models import produto

# Register your models here.

class admin_produto(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fields = ['nome']

admin.site.register(produto,admin_produto)