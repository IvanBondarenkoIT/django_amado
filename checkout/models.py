from django.db import models
from django.core.validators import RegexValidator
from home.models import Product

import cart.models


class Order(models.Model):
    phone_validator = RegexValidator(regex=r'^+?3?8?0?\d{2}[- ]?(\d[- ]?){7}$',
                                     message='Phone number incorrect')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    city = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=50, blank=True)
    is_processed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(cart.models.Order, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name} {self.phone}: {self.comment[:20]}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.item.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_item', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
