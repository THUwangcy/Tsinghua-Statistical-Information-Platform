# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20161026_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_fillincheck',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_fillinhint',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
