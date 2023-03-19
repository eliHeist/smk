from django.contrib import admin

from accounts.models import Customer, CustomerGroup, User

# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(CustomerGroup)