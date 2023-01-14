from django.shortcuts import render
from .models import Product, ProductsCategory, ProductsBrand



# Create your views here.
def home(request):
    categories = ProductsCategory.objects.filter(is_visible=True)
    products = Product.objects.filter(available=True)

    return render(request, 'index.html')


