# Generated by Django 4.2.5 on 2023-09-20 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='imagem',
            field=models.FileField(upload_to='imagem_carro'),
        ),
    ]
