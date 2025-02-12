# Generated by Django 5.0.7 on 2024-10-07 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookings", "0005_alter_booking_options_alter_booking_customer_bill_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="bookings",
                to="bookings.bookingstatus",
            ),
        ),
    ]
