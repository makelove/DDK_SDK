# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 14:47
# @Author  : play4fun
# @File    : DdkGoodsPidQuery.py
# @Software: PyCharm

"""
DdkGoodsPidQuery.py:
查询已经生成的推广位信息
"""

from ddk.api.base import RestApi


class DdkGoodsPidQuery(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.page_size = None  # 返回的每页推广位数量
        self.page = None  #

    def getapiname(self):
        return 'pdd.ddk.goods.pid.query'
