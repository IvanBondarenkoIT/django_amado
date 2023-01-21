from django.shortcuts import render
from home.models import Product, ProductsCategory, ProductsBrand

from cart.cart import Cart

from .forms import OrderCreateForm
from .models import OrderItem


def checkout(request):
    cart = Cart(request)
    # categories = ProductsCategory.objects.filter(is_visible=True)
    # brands = ProductsBrand.objects.filter(is_visible=True)
    products = Product.objects.filter(available=True)

    return render(request, 'checkout.html', context={'products': products, 'cart': cart})



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
                #clear the cart
                cart.clear()
                return render(request, 'created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'create.html', {'cart': cart, 'form': form})