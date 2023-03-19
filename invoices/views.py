import json
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from invoices.filters import InvoiceFilter
from invoices.models import Invoice
from django.core import serializers

# Create your views here.

def invoiceListView(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('accounts:login')
    invoices = Invoice.objects.all().order_by('-date').order_by('-time')
    Filter = InvoiceFilter(request.GET, queryset=invoices)
    invoices = Filter.qs
    listarray = []
    for invoice in invoices:
        orders = invoice.orders.all()
        for order in orders:
            order_item_price = order.selling_price
            order_quantity = order.quantity
            order.final_cost = order_item_price * order_quantity
        invoice.all_orders = orders
        total = sum(order.selling_price*order.quantity for order in orders)
        invoice.total_cost = total
        items = sum(order.quantity for order in orders)
        invoice.items_total = items
        inv = {'date':str(invoice.date.strftime("%a %d %b %Y")), 'sales':total}
        def searchDate(date, sale):
            for object in listarray:
                if object.get('date') == date:
                    object.update({'sales': object.get('sales')+sale})
                    return 0
            inv = {'date':date, 'sales':sale}
            listarray.append(inv)
            return 1
        searchDate(str(invoice.date.strftime("%a %d %b %Y")), total)
    
    # print(f'\n{listarray}\n')
    # jsonobj = serializers.serialize('json', invoices)
    

    context = {
        'invoices':invoices,
        'filter':Filter,
        'data': json.dumps(listarray)
    }
    return render(request, template_name="invoices/transactions.html", context=context)
