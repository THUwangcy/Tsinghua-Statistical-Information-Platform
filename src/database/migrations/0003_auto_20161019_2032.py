# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20161013_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='questionaire_type',
            new_name='question_types',
        ),
        migrations.AddField(
            model_name='question',
            name='question_choices',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='question_order',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='questionaire',
            name='questionaire_status',
            field=models.CharField(default=b'IN', max_length=2, choices=[(b'IN', b'initial'), (b'SA', b'saved'), (b'LA', b'lauched')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(),
        ),
    ]
