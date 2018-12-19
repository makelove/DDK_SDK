# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 11:47
# @Author  : play4fun
# @File    : __init__.py.py
# @Software: PyCharm

"""
__init__.py.py:
"""

__version__ = '18.12.19'
__author__ = 'play4fun <play4fun@foxmail.com>'

from ddk.api.base import sign


class appinfo(object):
    def __init__(self, appkey, secret):
        self.appkey = appkey
        self.secret = secret


def getDefaultAppInfo():
    pass


def setDefaultAppInfo(appkey, secret):
    default = appinfo(appkey, secret)
    global getDefaultAppInfo
    getDefaultAppInfo = lambda: default
