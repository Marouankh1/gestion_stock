from django.contrib import admin
from .models import Category, Product

# Enregistrement les models dans Django Admin
admin.site.register(Category)
admin.site.register(Product)