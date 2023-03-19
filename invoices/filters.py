from django import forms
from django_filters import FilterSet, DateFilter

from invoices.models import Invoice

class InvoiceFilter(FilterSet):
    from_date = DateFilter(field_name='date', lookup_expr='gte')
    to_date = DateFilter(field_name='date', lookup_expr='lte')
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['discount', 'time']