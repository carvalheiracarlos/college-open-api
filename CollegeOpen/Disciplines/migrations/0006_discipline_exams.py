# Generated by Django 3.1.8 on 2022-07-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disciplines', '0005_discipline_educational_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipline',
            name='exams',
            field=models.PositiveSmallIntegerField(default=3, verbose_name='Quantidade de Avaliações'),
        ),
    ]
