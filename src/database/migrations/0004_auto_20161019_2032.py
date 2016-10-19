# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20161019_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_types',
            new_name='question_type',
        ),
    ]
