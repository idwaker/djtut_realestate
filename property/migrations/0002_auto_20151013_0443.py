# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 10, 13, 4, 43, 8, 797875, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 10, 13, 4, 43, 16, 30158, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
