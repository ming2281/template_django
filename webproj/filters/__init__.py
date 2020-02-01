#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/6/29
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from django_filters import rest_framework as filters
import django_filters

from webproj.models import Goods


class GoodsFilter(filters.FilterSet):
    age_min = django_filters.NumberFilter(field_name='age', lookup_expr='gte')
    age_max = django_filters.NumberFilter(field_name='age', lookup_expr='lte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ["age_min", 'age_max', 'name']
