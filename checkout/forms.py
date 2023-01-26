from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'address', 'comment']

    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                                'type': "text",
                                                'name': "first_name",
                                                'class': "form-control",
                                                'id': "first_name",
                                                'placeholder': "First Name",
                                                'data-rule': "minlen:4",
                                                'data-msg': "Please enter at least 4 chars"
    }))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                                'type': "text",
                                                'name': "last_name",
                                                'class': "form-control",
                                                'id': "last_name",
                                                'placeholder': "Last Name",
                                                'data-rule': "minlen:4",
                                                'data-msg': "Please enter at least 4 chars"

    }))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
                                                'type': "email",
                                                'name': "email",
                                                'class': "form-control",
                                                'id': "email",
                                                'placeholder': "Email",
                                                'data-rule': "minlen:4",
                                                'data-msg': "Please enter at least 4 chars"

    }))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
                                                'type': "text",
                                                'name': "phone",
                                                'class': "form-control",
                                                'id': "phone",
                                                'placeholder': "Phone",
                                                'data-rule': "minlen:4",
                                                'data-msg': "Please enter at least 4 chars"

    }))
    city = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                                'type': "text",
                                                'name': "city",
                                                'class': "form-control",
                                                'id': "city",
                                                'placeholder': "City",
                                                'data-rule': "minlen:4",
                                                'data-msg': "Please enter at least 4 chars"

    }))
    address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                                'type': "text",
                                                'name': "address",
                                                'class': "form-control",
                                                'id': "address",
                                                'placeholder': "Address",
                                                'data-rule': "minlen:4",
                                                'data-msg': "Please enter at least 4 chars"

    }))
    comment = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                                'type': "text",
                                                'name': "comment",
                                                'class': "form-control",
                                                'id': "comment",
                                                'placeholder': "Comment",
                                                'data-rule': "minlen:4",
                                                'data-msg': "Please enter at least 4 chars"

    }))
