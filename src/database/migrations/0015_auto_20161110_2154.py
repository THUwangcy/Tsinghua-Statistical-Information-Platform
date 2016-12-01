# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_auto_20161110_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default=b'', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='identity',
            field=models.CharField(default=b'legalUser', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'00000000', max_length=32),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=b'ah', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default=b'', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(default=b'88888888', max_length=20),
        ),
    ]
