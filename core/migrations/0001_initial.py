# Generated by Django 3.1.4 on 2021-01-12 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('dataInicio', models.DateField(auto_now_add=True)),
                ('dataTermino', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('risco', models.IntegerField()),
                ('tipo', models.CharField(max_length=255)),
                ('retornoEsperado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('participantes', models.CharField(max_length=255)),
            ],
        ),
    ]