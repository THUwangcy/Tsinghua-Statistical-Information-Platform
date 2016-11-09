# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_auto_20161110_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionaire',
            name='questionaire_status',
            field=models.CharField(default=b'IN', max_length=2, choices=[(b'IN', b'initial'), (b'SA', b'saved'), (b'LA', b'lauched'), (b'PA', b'pause')]),
        ),
    ]
