# Generated by Django 4.0.3 on 2022-04-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0007_rename_item_price_order_selling_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='created_at',
            new_name='date_created',
        ),
        migrations.AddField(
            model_name='invoice',
            name='time_created',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
