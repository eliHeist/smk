from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=True)
    customer_account = models.ForeignKey('Customer', on_delete=models.DO_NOTHING, null=True)


class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    card_number = models.PositiveIntegerField(unique=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey("CustomerGroup", on_delete=models.SET_NULL, null=True, related_name='customers', default=1)

    def __str__(self) -> str:
        return self.name or "Customer"


class CustomerGroup(models.Model):
    name = models.CharField(max_length=50)
    discount = models.FloatField()

    def __str__(self) -> str:
        return self.name
