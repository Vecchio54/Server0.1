# Generated by Django 4.2.15 on 2024-08-22 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('computador', '0003_alter_computer_switch_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='usuarioa',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='historicalcomputer',
            old_name='usuarioa',
            new_name='usuario',
        ),
    ]
