# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_auto_20161117_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_displayVotes',
            field=models.BooleanField(default=True),
        ),
    ]
