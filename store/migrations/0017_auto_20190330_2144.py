# Generated by Django 2.1.7 on 2019-03-30 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20190330_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='total_score',
            field=models.IntegerField(),
        ),
    ]
