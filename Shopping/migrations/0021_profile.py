# Generated by Django 4.0.3 on 2022-04-14 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0020_remove_customer_address_remove_customer_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='static/images/user.png', upload_to='static/UserProfile')),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shopping.customer')),
            ],
        ),
    ]