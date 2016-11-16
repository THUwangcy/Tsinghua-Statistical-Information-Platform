# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_questionaire_questionaire_md5'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_hasPicture',
            field=models.IntegerField(default=False),
        ),
    ]
