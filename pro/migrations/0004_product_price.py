# Generated by Django 5.0.1 on 2024-11-17 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
