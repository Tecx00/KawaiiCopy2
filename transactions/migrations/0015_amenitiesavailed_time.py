# Generated by Django 5.0.7 on 2024-09-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0014_remove_amenities_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='amenitiesavailed',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
