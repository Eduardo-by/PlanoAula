# Generated by Django 4.2.3 on 2023-07-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanoAula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=1000)),
                ('descricao', models.TextField()),
                ('materiais', models.TextField()),
                ('objetivos', models.TextField()),
                ('referencias', models.TextField()),
                ('dia_criacao', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'PlanoAula',
                'verbose_name_plural': 'PlanoAulas',
            },
        ),
    ]