# Generated by Django 2.1.7 on 2019-03-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20190330_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_img'),
        ),
    ]
