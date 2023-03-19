from django.forms import ModelForm

from invoices.models import Invoice


class InvoiceCreationForm(ModelForm):
    class Meta:
        model = Invoice
        fields = {'handled_by'}

