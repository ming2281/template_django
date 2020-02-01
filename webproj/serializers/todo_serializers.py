#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/9/15
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from rest_framework import serializers

from webproj.models import TodoItem


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem

        fields = ('title', 'desc', "id", "create_time", "update_time")
