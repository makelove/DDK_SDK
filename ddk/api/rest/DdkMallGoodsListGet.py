# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 16:54
# @Author  : play4fun
# @File    : DdkMallGoodsListGet.py
# @Software: PyCharm

"""
DdkMallGoodsListGet.py:
http://open.pinduoduo.com/#/apidocument/port?id=179

查询店铺商品
"""

from ddk.api.base import RestApi


class DdkMallGoodsListGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.mall_id = None  # 店铺id
        self.page_number = None  # 分页数
        self.page_size = None  # 返回的每页推广位数量

    def getapiname(self):
        return 'pdd.ddk.mall.goods.list.get'
