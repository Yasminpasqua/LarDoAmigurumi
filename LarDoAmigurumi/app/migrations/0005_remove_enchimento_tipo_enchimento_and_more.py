# Generated by Django 5.1.5 on 2025-02-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_materiais_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enchimento',
            name='tipo_enchimento',
        ),
        migrations.RemoveField(
            model_name='enchimento',
            name='quantidade',
        ),
        migrations.AddField(
            model_name='enchimento',
            name='nome',
            field=models.CharField(default=1, max_length=100, verbose_name='Nome'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tipo_enchimento',
        ),
    ]
