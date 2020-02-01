#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/6/28
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now=True, null=False, blank=False)
    update_time = models.DateTimeField(auto_now=True, null=False, blank=False)

    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    name = models.CharField(max_length=30, )
    birthday = models.DateTimeField(null=True)
    gender = models.SmallIntegerField(null=True)

    create_time = models.DateTimeField(null=True, )
    update_time = models.DateTimeField(null=True, )


class TodoItem(BaseModel):
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=2000)

from setuptools import setup, find_packages
from setuptools.extension import  Extension
from Cython.Build import cythonize