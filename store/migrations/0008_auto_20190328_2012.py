# Generated by Django 2.1.7 on 2019-03-28 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20190328_2011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='product_des',
            new_name='product',
        ),
    ]
