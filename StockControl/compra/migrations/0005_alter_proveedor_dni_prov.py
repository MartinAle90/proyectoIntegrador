# Generated by Django 5.0.3 on 2024-03-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0004_producto_precio_prod_producto_stock_actual_prod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='dni_Prov',
            field=models.IntegerField(default=0, verbose_name='Dni'),
        ),
    ]