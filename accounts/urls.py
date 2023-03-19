import imp
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import CashierListView, CustomerCreateView, CustomerListView, SignupView

app_name = 'accounts'

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/add/', CustomerCreateView.as_view(), name='customer-create'),
    path('cashiers/', CashierListView.as_view(), name='cashier-list'),
    # authentication
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]