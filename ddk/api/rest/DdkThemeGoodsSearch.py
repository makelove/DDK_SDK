# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 17:09
# @Author  : play4fun
# @File    : DdkThemeGoodsSearch.py
# @Software: PyCharm

"""
DdkThemeGoodsSearch.py:
"""

from ddk.api.base import RestApi


class DdkThemeGoodsSearch(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        #
        self.theme_id = None  # 主题ID

    def getapiname(self):
        return 'pdd.ddk.theme.goods.search'
