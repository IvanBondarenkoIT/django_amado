from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'address', 'comment']

        # first_name = models.CharField(max_length=50)
        # last_name = models.CharField(max_length=50)
        # email = models.EmailField(max_length=50, blank=True)
        # phone = models.CharField(max_length=20, validators=[phone_validator])
        # city = models.CharField(max_length=50, blank=True)
        # address = models.CharField(max_length=50, blank=True)
        # comment = models.CharField(max_length=50, blank=True)
        # is_processed = models.BooleanField(default=False)
        # created = models.DateTimeField(auto_now_add=True)
        # modified = models.DateTimeField(auto_now=True)
        # order = models.ForeignKey(cart.models.Order, on_delete=models.CASCADE)
        # paid = models.BooleanField(default=False)