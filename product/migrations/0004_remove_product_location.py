# Generated by Django 2.2 on 2021-07-18 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210717_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='location',
        ),
    ]
