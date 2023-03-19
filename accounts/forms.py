from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import ModelForm

from accounts.models import Customer

User = get_user_model()

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name","last_name","username","email","is_manager","is_cashier",)
        field_classes = {'username': UsernameField}


class CustomerCreationForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']

