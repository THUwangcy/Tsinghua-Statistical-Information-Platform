# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_question_question_fillinrow'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_fillincheck',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_fillinhint',
            field=models.IntegerField(max_length=200, null=True),
        ),
    ]
