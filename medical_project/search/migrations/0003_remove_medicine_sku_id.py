# Generated by Django 3.2.9 on 2021-11-16 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_medicine_sku_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='sku_id',
        ),
    ]
