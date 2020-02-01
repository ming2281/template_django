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


class TodoItemListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
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

    def list(self, request, *args, **kwargs):
        """列举出所有todo项目

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        LOG.info(f'list start. {request}, {args} {kwargs}')

        result = super(TodoItemListViewSet, self).list(request, *args, **kwargs)

        LOG.info(f'will return. {result}')
        return result

    def create(self, request, *args, **kwargs):
        """创建一个todo项目

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        result = super(TodoItemListViewSet, self).create(request, *args, **kwargs)

        LOG.info(f'create will return {result}  {request}  {args}  {kwargs}')

        return result

    def retrieve(self, request, *args, **kwargs):
        """获取其中一个todo项目

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        result = super(TodoItemListViewSet, self).retrieve(request, *args, **kwargs)

        LOG.info(f'retrieve will return. {result}  {request}  {args}  {kwargs}')
        return result

    def update(self, request, *args, **kwargs):
        """更新一个todo项目

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        result = super(TodoItemListViewSet, self).update(request, *args, **kwargs)

        LOG.info(f'update will return. {result}  {request}  {args}  {kwargs}')
        return result

    def destroy(self, request, *args, **kwargs):
        """删除一个todo项目

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        result = super(TodoItemListViewSet, self).destroy(request, *args, **kwargs)

        LOG.info(f'destroy will return. {result}  {request}  {args}  {kwargs}')
        return result
