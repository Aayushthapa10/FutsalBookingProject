# Generated by Django 4.0.1 on 2022-02-20 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0012_order_address_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]