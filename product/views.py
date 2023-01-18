from django.shortcuts import render, get_object_or_404
from home.models import Product
import random


def product_list(request):
    products = Product.objects.filter(available=True)
    product = random.choice(products)
    return render(request, 'product-details.html', context={'product': product})


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'product-details.html', context={'product': product})
