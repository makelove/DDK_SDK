# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 16:03
# @Author  : play4fun
# @File    : GoodsCatsGet.py
# @Software: PyCharm

"""
GoodsCatsGet.py:
http://open.pinduoduo.com/#/apidocument/port?id=17

获取拼多多标准商品类目信息（请使用pdd.goods.authorization.cats接口获取商家可发布类目）
"""

from ddk.api.base import RestApi


class GoodsCatsGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        #
        self.parent_cat_id = None  # 值=0时为顶点cat_id,通过树顶级节点获取cat树

    def getapiname(self):
        return 'pdd.goods.cats.get'
