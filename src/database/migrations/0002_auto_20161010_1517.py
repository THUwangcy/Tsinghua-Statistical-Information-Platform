# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questionaire_title', models.CharField(max_length=40)),
                ('questionaire_time', models.DateTimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Student',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='student_id',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='questionaire',
            name='user',
            field=models.ForeignKey(to='database.User'),
        ),
    ]
