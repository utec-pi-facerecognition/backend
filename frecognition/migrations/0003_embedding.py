# Generated by Django 3.0.5 on 2020-05-18 03:40

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frecognition', '0002_admin_alumno_clases_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embedding',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('atributos', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=18, max_digits=18), size=None)),
            ],
        ),
    ]
