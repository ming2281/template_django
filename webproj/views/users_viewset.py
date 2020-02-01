#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/9/15
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from rest_framework import mixins
from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets
from webproj.models import TodoItem
from webproj.serializers import todo_serializers

import logging

LOG = logging.getLogger('CONSOLE')


class UsersViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                          mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    """
    TodoItem项管理, 增删改查

    list:
    获取所有todo项目
    """
    queryset = TodoItem.objects.all()
    serializer_class = todo_serializers.TodoSerializer


