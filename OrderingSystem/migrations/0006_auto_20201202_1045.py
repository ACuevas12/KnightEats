# Generated by Django 3.1.2 on 2020-12-02 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderingSystem', '0005_auto_20201202_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmenu',
            name='last_changed',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 2, 10, 45, 22, 325600)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 2, 10, 45, 22, 289666)),
        ),
    ]
