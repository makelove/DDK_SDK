# -*- coding: utf-8 -*-
# @Time    : 2018-12-10 15:12
# @Author  : play4fun
# @File    : DdkOrderDetailGet.py
# @Software: PyCharm

"""
DdkOrderDetailGet.py:
查询订单详情

"""

from ddk.api.base import RestApi


class DdkOrderDetailGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.order_sn = None  # 订单号

    def getapiname(self):
        return 'pdd.ddk.order.detail.get'
