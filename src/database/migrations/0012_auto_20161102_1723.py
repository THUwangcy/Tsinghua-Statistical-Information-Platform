# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20161102_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_choice',
            field=models.ForeignKey(to='database.Choice', null=True),
        ),
        migrations.AddField(
            model_name='filler',
            name='filler_address',
            field=models.CharField(default='\u5317\u4eac', max_length=50),
        ),
    ]
