# Generated by Django 5.0.6 on 2024-07-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_alter_cartitem_cart_alter_cartitem_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=30),
        ),
    ]