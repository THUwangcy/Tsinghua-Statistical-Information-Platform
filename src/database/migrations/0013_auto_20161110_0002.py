# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_auto_20161102_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_limit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_dayTimes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_displayVotes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='question',
            name='question_ipTimes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_time',
            field=models.CharField(default=b'2016', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_maxfill',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_minfill',
            field=models.IntegerField(null=True),
        ),
    ]
