# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 12:55
# @Author  : play4fun
# @File    : DdkGoodsDetail.py
# @Software: PyCharm

"""
DdkGoodsDetail.py:

https://open.pinduoduo.com/application/document/api?id=pdd.ddk.goods.detail&permissionId=2
"""

from ddk.api.base import RestApi


class DdkGoodsDetail(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)

        # self.goods_id_list = None  # 商品ID，仅支持单个查询。例如：[123456]
        self.goods_sign = None  # 商品goodsSign，支持通过goodsSign查询商品。goodsSign是加密后的goodsId, goodsId已下线，请使用goodsSign来替代。使用说明：https://jinbao.pinduoduo.com/qa-system?questionId=252

        self.pid = None  # 推广位id
        self.custom_parameters = None  # 自定义参数
        self.search_id = None  # 非必填	搜索id，建议填写，提高收益。来自pdd.ddk.goods.recommend.get、pdd.ddk.goods.search、pdd.ddk.top.goods.list.query等接口
        self.zs_duo_id = None  # 非必填	招商多多客ID

    def getapiname(self):
        return 'pdd.ddk.goods.detail'
