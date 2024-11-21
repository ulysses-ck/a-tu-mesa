# Generated by Django 5.1.2 on 2024-11-21 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesa', '0001_initial'),
        ('ticket', '0004_alter_ticket_promocion'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='estado',
            field=models.CharField(choices=[('Abierto', 'Abierto'), ('Cerrado', 'Cerrado')], default='Abierto', max_length=10),
        ),
        migrations.AddField(
            model_name='ticket',
            name='mesa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mesa.mesa'),
        ),
    ]
