# Generated by Django 3.1.8 on 2022-07-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academic', '0001_initial'),
        ('Disciplines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='students',
            field=models.ManyToManyField(blank=True, to='Academic.Student', verbose_name='Turma de Estudantes'),
        ),
    ]
