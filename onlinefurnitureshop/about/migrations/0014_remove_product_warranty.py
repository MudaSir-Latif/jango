# Generated by Django 5.0.6 on 2024-07-04 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0013_rename_waranty_product_warranty_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='warranty',
        ),
    ]
