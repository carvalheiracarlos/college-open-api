# Generated by Django 3.1.8 on 2022-07-19 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Disciplines', '0013_auto_20220719_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinereviews',
            name='discipline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Disciplines.discipline', verbose_name='Disciplina'),
        ),
    ]
