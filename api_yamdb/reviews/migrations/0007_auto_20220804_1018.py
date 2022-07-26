# Generated by Django 2.2.16 on 2022-08-04 10:18

import django.core.validators
from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20220803_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Значение должно быть от 1 до 10'), django.core.validators.MaxValueValidator(10, 'Значение должно быть от 1 до 10')], verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(db_index=True, validators=[reviews.validators.validate_year], verbose_name='Год'),
        ),
    ]
