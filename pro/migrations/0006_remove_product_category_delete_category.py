# Generated by Django 5.0.1 on 2024-11-24 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0005_alter_product_discription_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
