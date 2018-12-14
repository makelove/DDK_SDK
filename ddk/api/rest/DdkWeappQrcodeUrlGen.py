# -*- coding: utf-8 -*-
# @Time    : 2018-12-14 17:55
# @Author  : play4fun
# @File    : DdkWeappQrcodeUrlGen.py
# @Software: PyCharm

"""
DdkWeappQrcodeUrlGen.py:

http://open.pinduoduo.com/#/apidocument/port?id=106
多多客生成单品推广小程序二维码url
"""


from ddk.api.base import RestApi


class DdkWeappQrcodeUrlGen(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.p_id = None  # 推广位id
        self.goods_id_list = None  # 商品ID，仅支持单个查询
        self.custom_parameters = None  # 自定义参数
        self.zs_duo_id = None  # 招商多多客ID

    def getapiname(self):
        return 'pdd.ddk.weapp.qrcode.url.gen'
