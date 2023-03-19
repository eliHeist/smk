from pyexpat import model
from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, related_name='items', null=True)
    minimum_stock = models.PositiveIntegerField(default=10)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name