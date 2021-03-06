# Generated by Django 3.1.2 on 2020-12-02 02:13

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('OrderingSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmenu',
            name='changed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='itemmenu',
            name='last_changed',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 1, 21, 13, 22, 111901)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 1, 21, 13, 22, 74951)),
        ),
    ]
