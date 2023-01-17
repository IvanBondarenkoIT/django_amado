from django.shortcuts import render, get_object_or_404
from home.models import Product


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'product-details.html', context={'products': products})


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'product-details.html', context={'product': product})
