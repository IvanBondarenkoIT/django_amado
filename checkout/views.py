from django.shortcuts import render
from home.models import Product, ProductsCategory, ProductsBrand


def checkout(request):
    # categories = ProductsCategory.objects.filter(is_visible=True)
    # brands = ProductsBrand.objects.filter(is_visible=True)
    products = Product.objects.filter(available=True)

    return render(request, 'checkout.html', context={'products': products})
