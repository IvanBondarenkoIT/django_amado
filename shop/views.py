from django.shortcuts import render,  get_object_or_404
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


def _filter(request, id, class_name):
    cart = Cart(request)
    if class_name == 'ProductsBrand':
        filter_value = get_object_or_404(ProductsBrand, id=id, available=True)
        products = Product.objects.filter(available=True, brand=filter_value)
    elif class_name == 'ProductsCategory':
        filter_value = get_object_or_404(ProductsCategory, id=id, available=True)
        products = Product.objects.filter(available=True, category=filter_value)

    return render(request, 'shop.html', context={'products': products, 'cart': cart})
