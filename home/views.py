from django.shortcuts import render
from .models import Products, ProductsCategory, ProductsBrand
from django.http import HttpResponse


# Create your views here.
def home(request):
    categories = ProductsCategory.objects.all()
    return HttpResponse('\n'.join(map(str, categories)))


