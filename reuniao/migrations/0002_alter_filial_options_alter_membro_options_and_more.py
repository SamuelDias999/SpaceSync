# Generated by Django 5.0.4 on 2024-05-02 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reuniao', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filial',
            options={'verbose_name': 'Filial', 'verbose_name_plural': 'Filiais'},
        ),
        migrations.AlterModelOptions(
            name='membro',
            options={'verbose_name': 'Membro', 'verbose_name_plural': 'Membros'},
        ),
        migrations.AlterModelOptions(
            name='reuniao',
            options={'verbose_name': 'Reunião', 'verbose_name_plural': 'Reuniões'},
        ),
        migrations.AlterModelOptions(
            name='sala',
            options={'verbose_name': 'Sala', 'verbose_name_plural': 'Salas'},
        ),
        migrations.RemoveField(
            model_name='reuniao',
            name='membro',
        ),
    ]
