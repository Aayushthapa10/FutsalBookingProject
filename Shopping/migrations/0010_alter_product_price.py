# Generated by Django 4.0.1 on 2022-02-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0009_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
