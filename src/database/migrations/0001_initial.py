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
                ('questionaire_type', models.CharField(default=b'FI', max_length=2, choices=[(b'VO', b'vote'), (b'SI', b'single'), (b'FI', b'fillin'), (b'MU', b'multi'), (b'MA', b'mark'), (b'SO', b'sort')])),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Questionaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('questionaire_title', models.CharField(max_length=30)),
                ('questionaire_introduction', models.TextField(default='\u6ca1\u6709\u8bf4\u660e')),
                ('questionaire_type', models.CharField(default=b'SU', max_length=2, choices=[(b'VO', b'vote'), (b'LW', b'lab wanted'), (b'SU', b'sign up')])),
                ('questionaire_time', models.IntegerField()),
                ('questionaire_ip', models.GenericIPAddressField(null=True)),
                ('questionaire_numOfQues', models.IntegerField(default=0)),
                ('questionaire_numOfFilled', models.IntegerField(default=0)),
                ('questionaire_haveMaxTime', models.BooleanField(default=False)),
                ('questionaire_maxTime', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('student_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('real_name', models.CharField(max_length=20)),
                ('tel', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex=b'^\\d{3,12}$', message=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\x90\x88\xe6\xb3\x95\xe7\x9a\x84\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81')])),
                ('email', models.CharField(max_length=254, validators=[django.core.validators.EmailValidator(message=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\x90\x88\xe6\xb3\x95\xe7\x9a\x84\xe9\x82\xae\xe4\xbb\xb6\xe5\x9c\xb0\xe5\x9d\x80')])),
            ],
        ),
        migrations.AddField(
            model_name='questionaire',
            name='questionaire_user',
            field=models.ForeignKey(to='database.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='questionaire_id',
            field=models.ForeignKey(to='database.Questionaire'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='database.Question'),
        ),
    ]
