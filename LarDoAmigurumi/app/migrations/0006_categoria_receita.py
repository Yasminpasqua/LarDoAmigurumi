# Generated by Django 5.1.5 on 2025-02-03 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_enchimento_tipo_enchimento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('quantidade_linha', models.IntegerField(verbose_name='Quantidade de Linha')),
                ('passos', models.TextField(verbose_name='Passos')),
                ('dificuldade', models.CharField(max_length=50, verbose_name='Dificuldade')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoria', verbose_name='Categoria')),
                ('materiais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materiais', verbose_name='Materiais')),
            ],
            options={
                'verbose_name': 'Receita',
                'verbose_name_plural': 'Receitas',
            },
        ),
    ]
