# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 16:33
# @Author  : play4fun
# @File    : 多多客工具生成店铺推广链接API1.py
# @Software: PyCharm

"""
多多客工具生成店铺推广链接API1.py:

pdd.ddk.mall.url.gen
DdkMallUrlGen

"""

from ddk.api.rest.DdkMallUrlGen import DdkMallUrlGen
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret, pid


def test1():
    req = DdkMallUrlGen()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    #
    req.mall_id = 327071922
    req.pid = pid
    req.generate_short_url = True
    try:
        resp = req.getResponse()
        print(resp)
        print('-' * 40)
        print(json.dumps(resp))

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    '''
    {
    "mall_coupon_generate_url_response": {
        "list": [
            {
                "mobile_url": "https://mobile.yangkeduo.com/app.html?launch_url=duo_mall_coupon.html%3Fmall_id%3D327071922%26pid%3D1000939_25578619%26cpsSign%3DCW1000939_25578619_a16d7fc7cc017dd272eb69abe7db845f%26duoduo_type%3D2",
                "mobile_short_url": "https://p.pinduoduo.com/aTJmF5ZI",
                "we_app_web_view_url": "https://mobile.yangkeduo.com/duo_mall_coupon.html?mall_id=327071922&pid=1000939_25578619&cpsSign=CW1000939_25578619_a16d7fc7cc017dd272eb69abe7db845f&duoduo_type=2&launch_wx=1",
                "url": "https://mobile.yangkeduo.com/duo_mall_coupon.html?mall_id=327071922&pid=1000939_25578619&cpsSign=CW1000939_25578619_a16d7fc7cc017dd272eb69abe7db845f&duoduo_type=2",
                "short_url": "https://p.pinduoduo.com/A1dmTylb",
                "we_app_web_view_short_url": "https://p.pinduoduo.com/HX7mT8zd"
            }
        ],
        "request_id": "15451223844650882"
    }
}
    '''


if __name__ == '__main__':
    test1()
