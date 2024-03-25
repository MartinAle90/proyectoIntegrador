# Generated by Django 5.0.3 on 2024-03-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0003_alter_proveedor_dni_prov'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_Prod',
            field=models.IntegerField(default=0, max_length=10, verbose_name='Precio'),
        ),
        migrations.AddField(
            model_name='producto',
            name='stock_actual_Prod',
            field=models.CharField(default=0, max_length=10, verbose_name='Stock'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='apellido_Prov',
            field=models.CharField(default='apellido proveedor', max_length=100, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='dni_Prov',
            field=models.IntegerField(default=0, max_length=10, verbose_name='Dni'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre_Prov',
            field=models.CharField(default='nombre proveedor', max_length=100, verbose_name='Nombre'),
        ),
    ]
