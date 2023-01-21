from django.shortcuts import render
from home.models import Product, ProductsCategory, ProductsBrand
from cart.cart import Cart


def shop(request):
    cart = Cart(request)
    categories = ProductsCategory.objects.filter(is_visible=True)
    brands = ProductsBrand.objects.filter(is_visible=True)
    products = Product.objects.filter(available=True)

    return render(request, 'shop.html', context={'products': products,
                                                 'categories': categories,
                                                 'brands': brands,
                                                 'cart': cart
                                                 })

    # products = Product.objects.filter(id__in=product_ids)
