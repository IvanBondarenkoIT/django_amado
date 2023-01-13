from django.contrib import admin
from .models import Products, ProductsCategory, ProductsBrand

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductsCategory)
admin.site.register(ProductsBrand)
