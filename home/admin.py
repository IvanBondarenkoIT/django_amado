from django.contrib import admin
from .models import Product, ProductsCategory, ProductsBrand


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price',
                    'quantity', 'rating', 'available', 'is_special',
                    'category', 'brand', 'created', 'updated']
    list_filter = ['available', 'category', 'brand', 'created', 'updated']
    list_editable = ['available']

    prepopulated_fields = {'slug': ('name',)}


# admin.site.register(Product)
admin.site.register(ProductsCategory)
admin.site.register(ProductsBrand)
