# Generated by Django 3.1.5 on 2021-01-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_conference_room_booking_app', '0004_auto_20210128_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_of_booking',
            field=models.DateField(),
        ),
    ]
