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
    real_name = models.CharField(max_length = 20, default = "michael jackson")
    
    age = models.CharField(max_length = 18, default = "18")
    status = models.CharField(max_length = 400, default = "hello world")
    address = models.CharField(max_length = 400, default = "china")
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
    INIT = "IN"
    SAVED = "SA"
    LAUNCHED = "LA"
    PAUSE = "PA"
    STATUS = (
        (INIT, "initial"),
        (SAVED, "saved"),
        (LAUNCHED, "lauched"),
        (PAUSE, "pause")
        )
    questionaire_user = models.ForeignKey(User)
    questionaire_title = models.CharField(max_length = 30)
    questionaire_introduction = models.TextField(default = u"没有说明")
    questionaire_status = models.CharField(max_length = 2, choices = STATUS, default = INIT)
    questionaire_type = models.CharField(max_length = 2, choices = TYPES, default = SIGN_UP)
    questionaire_time = models.CharField(max_length = 50, default = "2016")
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
    question_text = models.TextField(default = u"请在此输入问题标题")
    question_type = models.CharField(max_length = 2, choices = TYPES, default = FILLIN)
    question_order = models.IntegerField(default = 1)
    question_choices = models.IntegerField(default = 0)
    question_time = models.CharField(max_length = 20, default = "2016")
    question_fillinrow = models.IntegerField(default = 1)
    question_fillinhint = models.CharField(max_length = 200, default = u"文本")
    question_fillincheck = models.CharField(max_length = 100, default = "")
    question_mustfill = models.BooleanField(default = False)
    question_minfill = models.IntegerField(null = True)
    question_maxfill = models.IntegerField(null = True)
    question_displayVotes = models.BooleanField(default = False)
    question_ipTimes = models.IntegerField(null = True)
    question_dayTimes = models.IntegerField(null = True)
    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length = 200)
    choice_order = models.IntegerField(default = 0)
    choice_limit = models.IntegerField(null = True)
    votes = models.IntegerField(default = 0)

    def __unicode__(self):
        return self.choice_text


class Filler(models.Model):
    filler_ip = models.CharField(max_length = 30, default = "0.0.0.0")
    filler_time = models.CharField(max_length = 30, default = "2016")
    filler_address = models.CharField(max_length = 50, default = u"北京")
    #filler_order = models.IntegerField(default = 1)
    filler_questionaire = models.ForeignKey(Questionaire)

class Answer(models.Model):
    answer_filler = models.ForeignKey(Filler)
    answer_question = models.ForeignKey(Question)
    answer_content = models.TextField(null = True)
    answer_choice = models.ForeignKey(Choice, null = True)
