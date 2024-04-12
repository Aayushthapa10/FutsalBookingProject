# Generated by Django 5.0.3 on 2024-03-15 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Infofutsal', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(blank=True, default='static/images/reviewphoto/review.jpg', null=True, upload_to='static/images/reviewphoto'),
        ),
        migrations.AlterField(
            model_name='review',
            name='message',
            field=models.CharField(max_length=1000),
        ),
    ]