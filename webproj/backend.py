#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/6/28
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username))
            if user.check_password(password):
                return user
        except Exception as e:

            return None
