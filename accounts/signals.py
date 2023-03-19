import random
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Customer, User


@receiver(post_save, sender=User)
def createUsersCustomerProfile(sender, instance, created, **kwargs):
    email = instance.email
    name = f'{instance.first_name} {instance.last_name}'
    if created:
        customer_profile = Customer.objects.create(name=name, email=email)
        User.objects.filter(id=instance.id).update(customer_account=customer_profile)
        print('profile created')
    elif not instance.is_superuser:
        Customer.objects.filter(id=instance.customer_account.id).update(name=name, email=email)


@receiver(post_save, sender=Customer)
def setCustomerNumber(sender, created, instance, **kwargs):
    if created:
        card = get_card()
        try:
            Customer.objects.filter(id=instance.id).update(card_number=card)
        except: 
            Customer.objects.filter(id=instance.id).update(card_number=get_card())
            
def get_card():
    return random.randint(1,999999)
