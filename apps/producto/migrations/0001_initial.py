# Generated by Django 5.1.2 on 2024-10-11 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipoProducto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipoProducto.tipoproducto')),
            ],
        ),
    ]