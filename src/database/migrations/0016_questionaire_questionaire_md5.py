# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_auto_20161110_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionaire',
            name='questionaire_md5',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
