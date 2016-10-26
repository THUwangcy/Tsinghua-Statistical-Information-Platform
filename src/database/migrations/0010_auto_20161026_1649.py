# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_auto_20161026_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_fillincheck',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_fillinhint',
            field=models.CharField(default='\u6587\u672c', max_length=200),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(default='\u8bf7\u5728\u6b64\u8f93\u5165\u95ee\u9898\u6807\u9898'),
        ),
    ]
