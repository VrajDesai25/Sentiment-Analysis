# Generated by Django 2.1.7 on 2019-03-28 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_products_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='product',
            new_name='product_id',
        ),
    ]
