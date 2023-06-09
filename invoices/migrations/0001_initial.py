# Generated by Django 4.0.3 on 2022-03-30 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_amount_paid', models.IntegerField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer')),
                ('handled_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('sold_at', models.DateTimeField(auto_now_add=True)),
                ('total_cost', models.IntegerField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='invoices.invoice')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='items.item')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.AddField(
            model_name='invoice',
            name='orders',
            field=models.ManyToManyField(related_name='orders', to='invoices.order'),
        ),
    ]
