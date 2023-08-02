# Generated by Django 4.2.3 on 2023-07-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plano_aula', '0002_alter_planoaula_dia_criacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planoaula',
            old_name='descricao',
            new_name='avaliacao',
        ),
        migrations.RenameField(
            model_name='planoaula',
            old_name='objetivos',
            new_name='conteudo',
        ),
        migrations.RenameField(
            model_name='planoaula',
            old_name='referencias',
            new_name='metodologia',
        ),
        migrations.AddField(
            model_name='planoaula',
            name='objetivo_geral',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planoaula',
            name='objetivos_especificos',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planoaula',
            name='referencias_basicas',
            field=models.TextField(default=312),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planoaula',
            name='referencias_complementar',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]