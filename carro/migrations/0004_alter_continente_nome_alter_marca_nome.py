# Generated by Django 4.2.5 on 2023-09-20 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0003_continente_marca_imagem_alter_carro_imagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continente',
            name='nome',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='nome',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]