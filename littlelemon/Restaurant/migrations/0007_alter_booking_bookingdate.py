# Generated by Django 3.2.20 on 2023-08-02 10:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0006_alter_booking_bookingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='BookingDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
