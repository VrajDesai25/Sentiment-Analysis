# Generated by Django 2.1.7 on 2019-03-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20190330_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='overall_rating',
            field=models.IntegerField(max_length=4),
        ),
    ]
