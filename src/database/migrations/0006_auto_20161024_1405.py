# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20161021_0756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_content', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Filler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filler_ip', models.CharField(default=b'0.0.0.0', max_length=30)),
                ('filler_time', models.CharField(default=b'2016', max_length=30)),
                ('filler_questionaire', models.ForeignKey(to='database.Questionaire')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_filler',
            field=models.ForeignKey(to='database.Filler'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_question',
            field=models.ForeignKey(to='database.Question'),
        ),
    ]
