# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20161026_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_maxfill',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='question',
            name='question_minfill',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='question_mustfill',
            field=models.BooleanField(default=False),
        ),
    ]
