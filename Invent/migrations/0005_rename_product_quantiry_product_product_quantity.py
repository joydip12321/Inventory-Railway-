# Generated by Django 4.2.5 on 2023-11-03 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Invent', '0004_remove_product_product_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_quantiry',
            new_name='Product_quantity',
        ),
    ]
