# Generated by Django 5.0.3 on 2024-03-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0006_alter_producto_precio_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='stock_actual_Prod',
            field=models.IntegerField(default=0, verbose_name='Stock'),
        ),
    ]
