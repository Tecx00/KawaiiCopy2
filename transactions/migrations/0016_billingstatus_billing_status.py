# Generated by Django 5.1.1 on 2024-10-02 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0015_amenitiesavailed_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='billing',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='transactions.billingstatus'),
        ),
    ]
