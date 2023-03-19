from multiprocessing import context
from django.views.generic import ListView
from django.shortcuts import render, redirect
from accounts.models import Customer
from items.models import Item

# Create your views here.



def landingPageView(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    items = Item.objects.all()
    customers = Customer.objects.all()
    context = {"items": items,"customers": customers}
    return render(request, 'main/landing.html', context=context)


class ItemListView(ListView):
    model = Item
    template_name = "invoices/product-list.html"

