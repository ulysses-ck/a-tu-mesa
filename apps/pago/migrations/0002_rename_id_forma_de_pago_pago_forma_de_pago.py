# Generated by Django 5.1.2 on 2024-10-29 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pago',
            old_name='id_forma_de_pago',
            new_name='forma_de_pago',
        ),
    ]
