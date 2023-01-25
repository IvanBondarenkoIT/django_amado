from django import forms
from .models import Order
from django.core.validators import RegexValidator


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'address', 'comment']

    phone_validator = RegexValidator(regex=r'^+?3?8?0?\d{2}[- ]?(\d[- ]?){7}$',
                                     message='Phone number incorrect')

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    phone = forms.CharField(widget=forms.TextInput(), validators=[phone_validator])
    city = forms.CharField(widget=forms.TextInput())
    address = forms.CharField(widget=forms.TextInput())
    comment = forms.CharField(widget=forms.TextInput())
