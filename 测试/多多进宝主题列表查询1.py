# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 17:03
# @Author  : play4fun
# @File    : 多多进宝主题列表查询1.py
# @Software: PyCharm

"""
多多进宝主题列表查询1.py:
pdd.ddk.theme.list.get
DdkThemeListGet

"""

from ddk.api.rest.DdkThemeListGet import DdkThemeListGet
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret


def test1():
    req = DdkThemeListGet()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    #
    req.page_size = 10
    req.page = 1

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
    "theme_list_get_response": {
        "total": 70,
        "theme_list": [
            {
                "image_url": "http://t16img.yangkeduo.com/pdd_oms/2018-12-17/2fde3277dfc3e9f896fe3873e2cdb681.jpg",
                "name": "俊狮男装品牌清仓！",
                "goods_num": 20,
                "id": 3975,
                "type": 1
            },
            {
                "image_url": "http://t16img.yangkeduo.com/pdd_oms/2018-12-16/eda7ba24a95a686472a91f9a6b6409d0.jpg",
                "name": "茜舞大牌返场 全场低至1折起",
                "goods_num": 21,
                "id": 3949,
                "type": 1
            },
            {
                "image_url": "http://t16img.yangkeduo.com/pdd_oms/2018-12-15/1ba0e848a1b143a25c22fe62615b15e3.jpg",
                "name": "印象童年保暖童装低至29元起",
                "goods_num": 19,
                "id": 3925,
                "type": 1
            },
            {
                "image_url": "http://t16img.yangkeduo.com/pdd_oms/2018-12-14/d0bcc58eb1f8955fa2a75c42c06f2816.jpg",
                "name": "喝好茶 送好礼",
                "goods_num": 70,
                "id": 3922,
                "type": 1
            },
            {
                "image_url": "http://t16img.yangkeduo.com/pdd_oms/2018-12-13/6741f085d1576406a47655fc60a9596f.jpg",
                "name": "卓诗尼冬日清仓1214",
                "goods_num": 17,
                "id": 3909,
                "type": 1
            },
            {
                "image_url": "http://t16img.yangkeduo.com/pdd_oms/2018-12-12/2c791099d407f0d6236c0ce0196e38b6.jpg",
                "name": "塔丹奴年终大促 打破底价1折起",
                "goods_num": 0,
                "id": 3897,
                "type": 1
            },
            {
                "image_url": "http://t16img.yangkeduo.com/pdd_oms/2018-12-12/76089cd44deb35b4b3671f578b3e2050.jpg",
                "name": "坚果暖冬大聚惠",
                "goods_num": 61,
                "id": 3564,
                "type": 1
            },
            {
                "image_url": "http://t16img.yangkeduo.com/pdd_oms/2018-12-11/d19a8df8e56e1993dd82e79e097916fb.jpg",
                "name": "jeepspirit男装清仓1212",
                "goods_num": 18,
                "id": 3877,
                "type": 1
            },
            {
                "image_url": "http://t16img.yangkeduo.com/pdd_oms/2018-12-10/805378efa93909c3b194743544218dd3.jpg",
                "name": "one more 低至0.6折起",
                "goods_num": 15,
                "id": 3857,
                "type": 1
            },
            {
                "image_url": "http://t16img.yangkeduo.com/pdd_oms/2018-12-09/c5c943f4a5c4c4bb15cb4c58b19c8bf5.jpg",
                "name": "芊艺女装 品牌特卖1折起",
                "goods_num": 24,
                "id": 3841,
                "type": 1
            }
        ],
        "request_id": "15451240342488254"
    }
}
    '''

if __name__ == '__main__':
    test1()
