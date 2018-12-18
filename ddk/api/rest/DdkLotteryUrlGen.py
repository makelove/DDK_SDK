# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 14:42
# @Author  : play4fun
# @File    : DdkLotteryUrlGen.py
# @Software: PyCharm

"""
DdkLotteryUrlGen.py:
http://open.pinduoduo.com/#/apidocument/port?id=106

多多客生成转盘抽免单url
"""

from ddk.api.base import RestApi


class DdkLotteryUrlGen(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        #
        self.pid_list = None  # 推广位列表，例如：["60005_612"]
        self.generate_weapp_webview = None  # 是否生成唤起微信客户端链接，true-是，false-否，默认false
        self.generate_short_url = None  # 是否生成短链接，true-是，false-否
        self.multi_group = None  # true--生成多人团推广链接 false--生成单人团推广链接（默认false）1、单人团推广链接：用户访问单人团推广链接，可直接购买商品无需拼团。2、多人团推广链接：用户访问双人团推广链接开团，若用户分享给他人参团，则开团者和参团者的佣金均结算给推手
        self.custom_parameters = None  # 自定义参数，为链接打上自定义标签。自定义参数最长限制64个字节。

    def getapiname(self):
        return 'pdd.ddk.lottery.url.gen'
