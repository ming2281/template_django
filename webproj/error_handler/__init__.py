#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# date:        2019/6/29
# author:      he.zhiming
#

from __future__ import (absolute_import, unicode_literals)

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code
        # response.data.pop('detail')

    return response
