# -*- coding: utf-8 -*-
# @Time    : 2018-12-14 17:35
# @Author  : play4fun
# @File    : 多多进宝转链接口1.py
# @Software: PyCharm

"""
多多进宝转链接口1.py:
把别人的转链，转成自己的
"""

from ddk.api.rest.DdkGoodsZsUnitUrlGen import DdkGoodsZsUnitUrlGen
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret, pid


def test1():
    req = DdkGoodsZsUnitUrlGen()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    # goods_id='4532814226,2478116379'#参数错误:只支持单个goodsId查询
    req.pid = pid
    # req.source_url = "https://p.pinduoduo.com/HXPmFuSx"
    req.source_url = "https://mobile.yangkeduo.com/duo_coupon_landing.html?goods_id=2478116379&pid=1000939_25578619&cpsSign=CC1000939_25578619_80c3d6ab8a4d5b1624dc5f3fa40ba9ff&duoduo_type=3"
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
    "goods_zs_unit_generate_response": {
        "multi_group_url": "https://mobile.yangkeduo.com/duo_coupon_landing.html?goods_id=2478116379&pid=1860931_43746459&cpsSign=CC1860931_43746459_01cb1d6f45ae5bc9d01581525853593e&duoduo_type=3",
        "multi_group_mobile_short_url": "https://p.pinduoduo.com/ctzmcX8k",
        "mobile_url": "https://mobile.yangkeduo.com/app.html?launch_url=duo_coupon_landing.html%3Fgoods_id%3D2478116379%26pid%3D1860931_43746459%26cpsSign%3DCC1860931_43746459_01cb1d6f45ae5bc9d01581525853593e%26duoduo_type%3D2",
        "multi_group_short_url": "https://p.pinduoduo.com/svsmce9Z",
        "mobile_short_url": "https://p.pinduoduo.com/DzKmcClj",
        "multi_group_mobile_url": "https://mobile.yangkeduo.com/app.html?launch_url=duo_coupon_landing.html%3Fgoods_id%3D2478116379%26pid%3D1860931_43746459%26cpsSign%3DCC1860931_43746459_01cb1d6f45ae5bc9d01581525853593e%26duoduo_type%3D3",
        "request_id": "15447806742539308",
        "url": "https://mobile.yangkeduo.com/duo_coupon_landing.html?goods_id=2478116379&pid=1860931_43746459&cpsSign=CC1860931_43746459_01cb1d6f45ae5bc9d01581525853593e&duoduo_type=2",
        "short_url": "https://p.pinduoduo.com/WF8mc1iB"
    }
}
    '''


if __name__ == '__main__':
    test1()
