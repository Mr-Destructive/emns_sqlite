# Generated by Django 3.2.5 on 2021-10-09 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduledmail',
            name='send_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 16, 34, 0, 699778)),
        ),
    ]
