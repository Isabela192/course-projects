# Generated by Django 4.0.3 on 2022-03-22 12:34
from __future__ import annotations

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='nome',
            new_name='codig_curso',
        ),
    ]
