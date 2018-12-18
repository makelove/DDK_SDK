# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 16:17
# @Author  : play4fun
# @File    : DdkMerchantListGet.py
# @Software: PyCharm

"""
DdkMerchantListGet.py:
http://open.pinduoduo.com/#/apidocument/port?id=179

多多客查店铺列表接口
"""

from ddk.api.base import RestApi


class DdkMerchantListGet(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        #
        self.mall_id_list = None  # 店铺id
        self.merchant_type_list = None  # 店铺类型
        self.query_range_str = None  # 查询范围0----商品拼团价格区间；1----商品券后价价格区间；2----佣金比例区间；3----优惠券金额区间；4----加入多多进宝时间区间；5----销量区间；6----佣金金额区间
        self.cat_id = None  # 商品类目ID，使用pdd.goods.cats.get接口获取
        self.has_coupon = None  # 是否有优惠券 （0 所有；1 必须有券。）
        self.page_number = None  # 分页数
        self.page_size = None  # 每页数量
        self.range_vo_list = None  # 筛选范围

    def getapiname(self):
        return 'pdd.ddk.merchant.list.get'
