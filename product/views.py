from django.shortcuts import render, get_object_or_404
from home.models import Product
from cart.cart import Cart
import random


def product_random(request):
    cart = Cart(request)
    products = Product.objects.filter(available=True)
    product = random.choice(products)
    return render(request, 'product-details.html', context={'product': product, 'cart': cart})


def product_details(request, id, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'product-details.html', context={'product': product, 'cart': cart})
