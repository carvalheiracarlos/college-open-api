# Generated by Django 3.1.8 on 2022-07-19 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Disciplines', '0012_auto_20220719_0607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disciplinereviews',
            old_name='disciplines',
            new_name='discipline',
        ),
    ]
