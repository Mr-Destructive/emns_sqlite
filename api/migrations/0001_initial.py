# Generated by Django 3.2.5 on 2021-10-09 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=78)),
                ('body', models.CharField(max_length=40000)),
                ('send_on', models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 9, 16, 33, 51, 54226))),
                ('recipients_list', models.CharField(max_length=1023)),
                ('attachment_file', models.FileField(blank=True, null=True, upload_to='mail/uploads/')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]