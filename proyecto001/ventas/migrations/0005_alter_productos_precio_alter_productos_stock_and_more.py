# Generated by Django 4.2.7 on 2023-12-03 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ventas", "0004_rename_subtotal_venta_preciounitario_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productos",
            name="precio",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="productos",
            name="stock",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="venta",
            name="PrecioUnitario",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="venta",
            name="cantidad",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="venta",
            name="total",
            field=models.IntegerField(),
        ),
    ]
