# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_question_question_haspicture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_hasPicture',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_hasPicture',
            field=models.BooleanField(default=False),
        ),
    ]
