# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 14:27
# @Author  : play4fun
# @File    : DdkGoodsPromotionUrlGenerate.py
# @Software: PyCharm

"""
DdkGoodsPromotionUrlGenerate.py:
生成普通商品推广链接
"""

from ddk.api.base import RestApi


class DdkGoodsPromotionUrlGenerate(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.goods_id_list = None  # 商品ID，仅支持单个查询。例如：[123456]
        self.p_id: int = None  # 推广位id
        self.generate_short_url = None  # 是否生成短链接，true-是，false-否
        self.multi_group = None  # true--生成多人团推广链接 false--生成单人团推广链接（默认false）1、单人团推广链接：用户访问单人团推广链接，可直接购买商品无需拼团。2、多人团推广链接：用户访问双人团推广链接开团，若用户分享给他人参团，则开团者和参团者的佣金均结算给推手
        self.custom_parameters = None  # 自定义参数，为链接打上自定义标签。自定义参数最长限制64个字节。
        self.pull_new = None  # 是否开启订单拉新，true表示开启（订单拉新奖励特权仅支持白名单，请联系工作人员开通）
        self.generate_weapp_webview = None  # 是否生成唤起微信客户端链接，true-是，false-否，默认false
        self.zs_duo_id = None  # 招商多多客ID
        self.generate_we_app: bool = None  # 是否生成小程序推广

    def getapiname(self):
        return 'pdd.ddk.goods.promotion.url.generate'
