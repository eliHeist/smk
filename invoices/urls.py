import imp
from django.urls import path

from invoices.views import invoiceListView

app_name = 'sales'

urlpatterns = [
    path('', invoiceListView, name='sales-list')
]