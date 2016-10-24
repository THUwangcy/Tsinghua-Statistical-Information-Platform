# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20161019_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=b'china', max_length=400),
        ),
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.CharField(default=b'18', max_length=18),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'00000000', max_length=32),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(default=b'hello world', max_length=400),
        ),
        migrations.AlterField(
            model_name='questionaire',
            name='questionaire_time',
            field=models.CharField(default=b'2016', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='real_name',
            field=models.CharField(default=b'michael jackson', max_length=20),
        ),
    ]
