# Generated by Django 3.2.9 on 2021-11-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='sku_id',
            field=models.IntegerField(null=True),
        ),
    ]
