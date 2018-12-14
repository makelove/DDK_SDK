# -*- coding: utf-8 -*-
# @Time    : 2018-12-14 17:36
# @Author  : play4fun
# @File    : DdkGoodsZsUnitUrlGen.py
# @Software: PyCharm

"""
DdkGoodsZsUnitUrlGen.py:
http://open.pinduoduo.com/#/apidocument/port?id=106
多多进宝转链接口

本功能适用于采集群等场景。将其他推广者的推广链接转换成自己的；
通过此api，可以将他人的招商推广链接，转换成自己的招商推广链接
"""

from ddk.api.base import RestApi


class DdkGoodsZsUnitUrlGen(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.source_url = None  # 需转链的链接
        self.pid: int = None  # 推广位id

    def getapiname(self):
        return 'pdd.ddk.goods.zs.unit.url.gen'
