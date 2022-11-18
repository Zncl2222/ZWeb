# Generated by Django 4.1.3 on 2022-11-13 07:04
from __future__ import annotations

import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameters_records',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('realizations_number', models.PositiveIntegerField()),
                ('cov_model', models.CharField(max_length=20)),
                (
                    'kernel',
                    models.CharField(
                        choices=[
                            ('Python', 'Python'),
                            ('C', 'C'),
                        ],
                        max_length=10,
                    ),
                ),
                ('bandwidth', models.FloatField()),
                ('bandwidth_step', models.FloatField()),
                ('x_size', models.IntegerField()),
                ('y_size', models.IntegerField()),
                ('randomseed', models.IntegerField()),
                ('krige_range', models.FloatField()),
                ('krige_sill', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Sgsim',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('results', models.JSONField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('run_time', models.FloatField()),
                (
                    'parameters',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='sgsim_app.parameters_records',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
