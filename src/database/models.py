# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.fields import FieldDoesNotExist
from django.core.validators import *
from django.core.exceptions import ValidationError, ObjectDoesNotExist, MultipleObjectsReturned
from django.conf import settings
import traceback

# Create your models here.
class Admin(models.Model):
    username = models.CharField(u'该用户名', max_length = 20, primary_key = True)
    description = models.CharField(max_length = 100, null = True)
    password = models.CharField(max_length = 32)
    email = models.CharField(max_length = 254)

    def __unicode__(self):
        return "%s: %s" % (self.username, self.description)


class User(models.Model):
    student_id = models.CharField(max_length = 20, primary_key = True)
    real_name = models.CharField(max_length = 20)
    tel = models.CharField(
        max_length = 20,
        validators = [
            RegexValidator(
                regex = r'^\d{3,12}$',
                message = '请输入合法的电话号码'
            )
        ]
    )
    email = models.CharField(
        max_length = 254,
        validators = [
            EmailValidator(
                message = '请输入合法的邮件地址'
            )
        ]
    )

    def __unicode__(self):
        return u'%s(%s)' % (self.user_id, self.real_name)

class Questionaire(models.Model):
    VOTE = "VO"
    LAB_WANTED = "LW"
    SIGN_UP = "SU"
    TYPES = (
        (VOTE, "vote"),
        (LAB_WANTED, "lab wanted"),
        (SIGN_UP, "sign up")
        )
    questionaire_user = models.ForeignKey(User)
    questionaire_title = models.CharField(max_length = 40)
    questionaire_introduction = models.TextField(default = u"没有说明")
    questionaire_type = models.CharField(max_length = 2, choices = TYPES, default = SIGN_UP)
    questionaire_time = models.IntegerField()
    questionaire_ip = models.GenericIPAddressField(null = True)
    questionaire_numOfQues = models.IntegerField(default = 0)
    questionaire_numOfFilled = models.IntegerField(default = 0)
    questionaire_haveMaxTime = models.BooleanField(default = False)
    questionaire_maxTime = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.id + self.questionaire_title


class Question(models.Model):
    SINGLE = "SI"
    MULTI = "MU"
    FILLIN = "FI"
    VOTE = "VO"
    MARK = "MA"
    SORT = "SO"
    TYPES = (
        (VOTE, "vote"),
        (SINGLE, "single"),
        (FILLIN, "fillin"),
        (MULTI, "multi"),
        (MARK, "mark"),
        (SORT, "sort")
        )
    questionaire_id = models.ForeignKey(Questionaire)
    question_text = models.CharField(max_length = 200)
    questionaire_type = models.CharField(max_length = 2, choices = TYPES, default = FILLIN)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.choice_text