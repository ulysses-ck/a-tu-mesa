# Generated by Django 5.1.1 on 2024-10-29 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comanda', '0002_rename_id_estado_comanda_estado_and_more'),
        ('ticket', '0003_remove_ticket_id_promocion_ticket_promocion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.ticket'),
        ),
    ]