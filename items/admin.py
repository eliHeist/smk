from django.contrib import admin

from items.models import Brand, Item

# Register your models here.
admin.site.register(Item)
admin.site.register(Brand)
