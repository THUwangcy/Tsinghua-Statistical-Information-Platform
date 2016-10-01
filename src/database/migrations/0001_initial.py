# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('username', models.CharField(max_length=20, serialize=False, verbose_name='\u8be5\u7528\u6237\u540d', primary_key=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('real_name', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=40)),
                ('tel', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^\\d{3,12}$', message=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\x90\x88\xe6\xb3\x95\xe7\x9a\x84\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81')])),
                ('email', models.CharField(max_length=254, validators=[django.core.validators.EmailValidator(message=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\x90\x88\xe6\xb3\x95\xe7\x9a\x84\xe9\x82\xae\xe4\xbb\xb6\xe5\x9c\xb0\xe5\x9d\x80')])),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='database.Question'),
        ),
    ]
