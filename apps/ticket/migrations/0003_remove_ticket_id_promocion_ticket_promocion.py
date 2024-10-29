# Generated by Django 5.1.2 on 2024-10-29 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promociones', '0002_rename_id_producto_condiciones_producto_and_more'),
        ('ticket', '0002_remove_ticket_id_promocion_ticket_id_promocion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='id_promocion',
        ),
        migrations.AddField(
            model_name='ticket',
            name='promocion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='promociones.promociones'),
            preserve_default=False,
        ),
    ]