# Generated by Django 3.1.5 on 2021-01-26 19:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('capacity', models.IntegerField(validators=[django.core.validators.MinValueValidator(2, message='Wartośc musi być większa od dwóch')])),
                ('projector', models.BooleanField(default=False)),
            ],
        ),
    ]
