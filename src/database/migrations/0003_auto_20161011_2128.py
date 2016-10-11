# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20161010_1517'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='student_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dept',
        ),
        migrations.AddField(
            model_name='questionaire',
            name='questionaire_haveMaxTime',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='questionaire',
            name='questionaire_introduction',
            field=models.TextField(default='\u6ca1\u6709\u8bf4\u660e'),
        ),
        migrations.AddField(
            model_name='questionaire',
            name='questionaire_ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(
            model_name='questionaire',
            name='questionaire_maxTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionaire',
            name='questionaire_numOfFilled',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionaire',
            name='questionaire_numOfQues',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='questionaire',
            name='questionaire_type',
            field=models.CharField(default=b'SU', max_length=2, choices=[(b'VO', b'vote'), (b'LW', b'lab wanted'), (b'SU', b'sign up')]),
        ),
    ]
