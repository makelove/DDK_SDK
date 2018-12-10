# -*- coding: utf-8 -*-
# @Time    : 2018-12-10 15:27
# @Author  : play4fun
# @File    : DdkGoodsPidGenerate.py
# @Software: PyCharm

"""
DdkGoodsPidGenerate.py:

创建多多进宝推广位
"""

from ddk.api.base import RestApi


class DdkGoodsPidGenerate(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.number = None  # 要生成的推广位数量，默认为10，范围为：1~100
        self.p_id_name_list = None  # 推广位名称，例如["1","2"]

    def getapiname(self):
        return 'pdd.ddk.goods.pid.generate'
