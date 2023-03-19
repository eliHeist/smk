from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, CreateView
from accounts.forms import CustomerCreationForm, SignupForm

from accounts.models import Customer

User = get_user_model()

# Create your views here.
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = "accounts/customer-list.html"



class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerCreationForm
    template_name = "accounts/customer-create.html"

    def get_success_url(self):
        return reverse('accounts:customer-list')



# Auth and accounts
class SignupView(LoginRequiredMixin, CreateView):
    template_name = 'registration/signup.html'
    form_class = SignupForm

    def get_success_url(self):
        return reverse('accounts:login')



class CashierListView(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'cashiers'
    template_name = "accounts/cashier-list.html"

    def get_queryset(self):
        return User.objects.filter(is_cashier=True, is_staff=False)
