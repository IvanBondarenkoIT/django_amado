from django.shortcuts import render
from .models import Product, ProductsCategory, ProductsBrand
from cart.cart import Cart

TOP_PRODUCTS_ON_HOME_PAGE = 9


# Create your views here.
def home(request):
    cart = Cart(request)
    categories = ProductsCategory.objects.filter(is_visible=True)
    products = Product.objects.filter(available=True)
    products = products[:TOP_PRODUCTS_ON_HOME_PAGE]

    return render(request, 'home.html', context={'products': products, 'cart': cart})


