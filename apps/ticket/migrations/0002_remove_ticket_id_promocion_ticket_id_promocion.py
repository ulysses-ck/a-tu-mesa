# Generated by Django 5.1.1 on 2024-10-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promociones', '0001_initial'),
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='id_promocion',
        ),
        migrations.AddField(
            model_name='ticket',
            name='id_promocion',
            field=models.ManyToManyField(to='promociones.promociones'),
        ),
    ]
