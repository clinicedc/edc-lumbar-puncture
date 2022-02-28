# Generated by Django 3.2.11 on 2022-02-25 01:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edc_csf', '0002_auto_20220225_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallpcsf',
            name='opening_pressure',
            field=models.IntegerField(blank=True, help_text='Units cm of H<sub>2</sub>O', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='lpcsf',
            name='opening_pressure',
            field=models.IntegerField(blank=True, help_text='Units cm of H<sub>2</sub>O', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
    ]
