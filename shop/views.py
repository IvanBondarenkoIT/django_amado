from django.shortcuts import render
from home.models import Product, ProductsCategory, ProductsBrand


def shop(request):
    categories = ProductsCategory.objects.filter(is_visible=True)
    brands = ProductsBrand.objects.filter(is_visible=True)
    products = Product.objects.filter(available=True)

    return render(request, 'shop.html', context={'products': products,
                                                 'categories': categories,
                                                 'brands': brands,
                                                 'range': range(10)
                                                 })

    # products = Product.objects.filter(id__in=product_ids)
