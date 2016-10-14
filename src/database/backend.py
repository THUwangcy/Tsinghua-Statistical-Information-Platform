# coding=utf-8

from models import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models import Q
from django.utils import timezone
from django.conf import settings
import datetime
import time
from multiprocessing import Process
import traceback

def get_applications_by_user(username):
    return {}


def get_student_by_id(username):
    return ''