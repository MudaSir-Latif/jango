# Generated by Django 5.0.6 on 2024-07-02 07:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('cart_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='about.cart')),
                ('colour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.colour')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.size')),
            ],
        ),
    ]
