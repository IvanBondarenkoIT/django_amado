from django.shortcuts import render
from .models import Product, ProductsCategory, ProductsBrand

TOP_PRODUCTS_ON_HOME_PAGE = 3


# Create your views here.
def home(request):
    categories = ProductsCategory.objects.filter(is_visible=True)
    products = Product.objects.filter(available=True)
    products = products[:TOP_PRODUCTS_ON_HOME_PAGE]

    return render(request, 'home.html', context={'products': products})


