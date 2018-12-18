# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 16:16
# @Author  : play4fun
# @File    : 多多客查店铺列表接口1.py
# @Software: PyCharm

"""
多多客查店铺列表接口1.py:
pdd.ddk.merchant.list.get

DdkMerchantListGet
"""

from ddk.api.rest.DdkMerchantListGet import DdkMerchantListGet
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret


def test1():
    req = DdkMerchantListGet()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    #
    req.mall_id_list = [1590059,327071922]
    try:
        resp = req.getResponse()
        print(resp)
        print('-' * 40)
        print(json.dumps(resp))

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())


if __name__ == '__main__':
    test1()
