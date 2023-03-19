import imp
from re import T
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Customer
from items.models import Item

User = get_user_model()

# Create your models here.
class Invoice(models.Model):
    # TODO: Define fields here
    time = models.TimeField(auto_now_add=True, null=True)
    date = models.DateField(auto_now_add=True)
    handled_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='employees')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'

    def __str__(self):
        return str(f'{self.handled_by.username}, {str(self.date)}')
    

class Order(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING, related_name='orders')
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING, null=True)
    selling_price = models.IntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField()
    sold_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        
        return str(f'{str(self.sold_at)[:16]}, {self.invoice.handled_by.username}')

@receiver(post_save, sender=Order)
def add_itemprice_to_order(sender, instance, created, **kwargs):
    if created:
        # instance.item_price
        price = instance.item.price
        Order.objects.filter(id=instance.id).update(selling_price=price)

@receiver(post_save, sender=Invoice)
def addDiscountToInvoice(sender, instance, created, **kwargs):
    # instance.discount
    if created and instance.customer:
        discount = instance.customer.group.discount
        Invoice.objects.filter(id=instance.id).update(discount=discount)