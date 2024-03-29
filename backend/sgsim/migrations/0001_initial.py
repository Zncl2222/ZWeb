# Generated by Django 4.2 on 2023-05-01 01:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SgsimParams',
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
                    models.CharField(choices=[('Python', 'Python'), ('C', 'C')], max_length=10),
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
            name='SgsimHistory',
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
                        to='sgsim.sgsimparams',
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
