from django.db import models
from django.core.validators import RegexValidator

import cart.models


class UserDelivery(models.Model):
    phone_validator = RegexValidator(regex=r'^+?3?8?0?\d{2}[- ]?(\d[- ]?){7}$',
                                     message='Phone number incorrect')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    address = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=50, blank=True)
    is_processed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(cart.models.Order, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.name} {self.phone}: {self.comment[:20]}'
