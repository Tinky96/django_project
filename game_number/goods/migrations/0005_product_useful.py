# Generated by Django 5.0.3 on 2024-05-15 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_remove_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='useful',
            field=models.BooleanField(default=True),
        ),
    ]
