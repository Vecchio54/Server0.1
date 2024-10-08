# Generated by Django 5.1.1 on 2024-09-23 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computador', '0004_rename_usuarioa_computer_usuario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='porta',
            field=models.CharField(choices=[('', 'selecione a porta'), ('Gi0/0', 'Gi0/0'), ('Gi0/1', 'Gi0/1'), ('Gi0/2', 'Gi0/2'), ('Gi0/3', 'Gi0/3'), ('gi1/0', 'gi1/0'), ('gi1/1', 'gi1/1'), ('gi1/2', 'Gi1/2'), ('gi1/3', 'Gi1/3')], max_length=8, verbose_name='Porta Switch'),
        ),
        migrations.AlterField(
            model_name='computer',
            name='voz',
            field=models.CharField(blank=True, choices=[('', 'seleciona rede de dados'), ('21', '21-voz Administração'), ('16', '16-voz Atendimento')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcomputer',
            name='porta',
            field=models.CharField(choices=[('', 'selecione a porta'), ('Gi0/0', 'Gi0/0'), ('Gi0/1', 'Gi0/1'), ('Gi0/2', 'Gi0/2'), ('Gi0/3', 'Gi0/3'), ('gi1/0', 'gi1/0'), ('gi1/1', 'gi1/1'), ('gi1/2', 'Gi1/2'), ('gi1/3', 'Gi1/3')], max_length=8, verbose_name='Porta Switch'),
        ),
        migrations.AlterField(
            model_name='historicalcomputer',
            name='voz',
            field=models.CharField(blank=True, choices=[('', 'seleciona rede de dados'), ('21', '21-voz Administração'), ('16', '16-voz Atendimento')], max_length=4, null=True),
        ),
    ]
