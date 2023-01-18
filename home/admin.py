from django.contrib import admin
from .models import Product, ProductsCategory, ProductsBrand


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'quantity', 'rating', 'available', 'is_special',
                    'category', 'brand', 'created', 'updated']
    list_filter = ['available', 'category', 'brand', 'created', 'updated']
    list_editable = ['available']

    prepopulated_fields = {'slug': ('name',)}


# admin.site.register(Product)
@admin.register(ProductsCategory)
class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible']
    list_filter = ['is_visible']
    list_editable = ['position', 'is_visible']


@admin.register(ProductsBrand)
class ProductsBrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible']
    list_filter = ['is_visible']
    list_editable = ['position', 'is_visible']

