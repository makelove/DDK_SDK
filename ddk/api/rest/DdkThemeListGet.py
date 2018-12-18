# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 17:05
# @Author  : play4fun
# @File    : DdkThemeListGet.py
# @Software: PyCharm

"""
DdkThemeListGet.py:
http://open.pinduoduo.com/#/apidocument/port?id=179

查询多多进宝主题列表
"""

from ddk.api.base import RestApi


class DdkThemeListGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        #
        self.page_size = None  #
        self.page = None  #

    def getapiname(self):
        return 'pdd.ddk.theme.list.get'
