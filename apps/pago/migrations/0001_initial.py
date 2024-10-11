# Generated by Django 5.1.2 on 2024-10-11 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaDePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_autorizacion', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('id_forma_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pago.formadepago')),
                ('pagador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.persona')),
            ],
        ),
    ]
