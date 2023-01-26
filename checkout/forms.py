from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'address', 'comment']

    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    phone = forms.CharField(widget=forms.TextInput())
    city = forms.CharField(widget=forms.TextInput())
    address = forms.CharField(widget=forms.TextInput())
    comment = forms.CharField(widget=forms.TextInput())
