# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20161024_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_fillinrow',
            field=models.IntegerField(default=1),
        ),
    ]
