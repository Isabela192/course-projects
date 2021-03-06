# Generated by Django 4.0.3 on 2022-04-25 22:30
from __future__ import annotations

import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_rename_codig_curso_curso_codigo_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                (
                    'id', models.BigAutoField(
                        auto_created=True,
                        primary_key=True, serialize=False, verbose_name='ID',
                    ),
                ),
                (
                    'periodo', models.CharField(
                        choices=[
                            ('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno'),
                        ], default='M', max_length=1,
                    ),
                ),
                (
                    'aluno', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='escola.aluno',
                    ),
                ),
                (
                    'curso', models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to='escola.curso',
                    ),
                ),
            ],
        ),
    ]
