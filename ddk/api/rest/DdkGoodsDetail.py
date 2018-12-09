# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 12:55
# @Author  : play4fun
# @File    : DdkGoodsDetail.py
# @Software: PyCharm

"""
DdkGoodsDetail.py:

https://open.pinduoduo.com/#/apidocument/port?id=27

"""

from ddk.api.base import RestApi


class DdkGoodsDetail(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.goods_id_list = None  # 商品ID，仅支持单个查询。例如：[123456]
        self.pid = None  # 推广位id
        self.custom_parameters = None  # 自定义参数

    def getapiname(self):
        return 'pdd.ddk.goods.detail'
