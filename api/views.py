
from datetime import datetime
from django.urls import reverse
from accounts.models import Customer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ItemSerializer

from invoices.models import Invoice, Order
from items.models import Item

# Create your views here.
@api_view(['POST'])
def salesApiView(request):
    array = request.data
    invoice = createInvoice(request.user)
    for order in array:
        # serializer = OrderSerializer(data=order)
        item = Item.objects.get(id=int(order.get('item')))
        neworder = Order.objects.create(item=item, quantity=int(order.get('quantity')),invoice=invoice)
        # update stock
        new_stock = item.stock - int(order.get('quantity'))
        Item.objects.filter(id=int(order.get('item'))).update(stock=int(new_stock))
    # update invoice with customer and discount used
    if order.get('customer') != 'none':
        customer = Customer.objects.get(id=int(order.get('customer')))
        Invoice.objects.filter(id=invoice.id).update(customer=customer, discount=customer.group.discount)
    

        
    return Response('success')

@api_view(['GET'])
def notificationView(request):
    allitems = Item.objects.all()
    items = []

    for item in allitems:
        if item.stock == 0:
            item.message = 'Out of stock'
            item.code = 'danger'
            items.append(item)
        elif item.stock < item.minimum_stock:
            item.message = 'Low stock'
            item.code = 'warning'
            items.append(item)

    serializer = ItemSerializer(items, many=True)

    
    return Response(serializer.data)



def createInvoice(cashier):
    if cashier:
        return Invoice.objects.create(handled_by=cashier,)

