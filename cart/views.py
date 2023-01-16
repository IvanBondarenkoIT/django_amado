from django.shortcuts import render
from home.models import Product, ProductsCategory, ProductsBrand


def cart(request):
    # categories = ProductsCategory.objects.filter(is_visible=True)
    # brands = ProductsBrand.objects.filter(is_visible=True)
    products = Product.objects.filter(available=True)

    return render(request, 'cart.html', context={'products': products})
