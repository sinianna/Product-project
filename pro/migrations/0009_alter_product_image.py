# Generated by Django 5.0.1 on 2024-11-24 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product_create'),
        ),
    ]
