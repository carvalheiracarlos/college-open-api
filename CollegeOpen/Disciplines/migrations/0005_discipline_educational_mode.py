# Generated by Django 3.1.8 on 2022-07-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Disciplines', '0004_discipline_compoent_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipline',
            name='educational_mode',
            field=models.SmallIntegerField(choices=[('0', 'PRESENCIAL'), ('1', 'REMOTO')], default=0, verbose_name='Modalidades de Educação'),
        ),
    ]
