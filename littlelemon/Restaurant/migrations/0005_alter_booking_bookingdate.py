# Generated by Django 3.2.20 on 2023-08-02 09:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0004_booking_bookingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 2, 9, 52, 59, 194060, tzinfo=utc)),
        ),
    ]