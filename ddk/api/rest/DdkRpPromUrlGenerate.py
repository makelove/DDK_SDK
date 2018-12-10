# -*- coding: utf-8 -*-
# @Time    : 2018-12-10 15:40
# @Author  : play4fun
# @File    : DdkRpPromUrlGenerate.py
# @Software: PyCharm

"""
DdkRpPromUrlGenerate.py:
生成红包推广链接
"""

from ddk.api.base import RestApi


class DdkRpPromUrlGenerate(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.generate_short_url = None  # 是否生成短链接，true-是，false-否
        self.p_id_list = None  # 推广位列表，例如：["60005_612"]
        self.custom_parameters = None  # 自定义参数，为链接打上自定义标签。自定义参数最长限制64个字节。
        self.generate_weapp_webview = None  # 是否生成唤起微信客户端链接，true-是，false-否，默认false
        self.we_app_web_view_short_url = None  # 唤起微信app推广短链接
        self.we_app_web_wiew_url = None  # 唤起微信app推广链接
        self.generate_we_app: bool = None  # 是否生成小程序推广

    def getapiname(self):
        return 'pdd.ddk.rp.prom.url.generate'
