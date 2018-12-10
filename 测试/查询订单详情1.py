# -*- coding: utf-8 -*-
# @Time    : 2018-12-10 15:13
# @Author  : play4fun
# @File    : 查询订单详情1.py
# @Software: PyCharm

"""
查询订单详情1.py:
"""


from ddk.api.rest.DdkOrderDetailGet import DdkOrderDetailGet
from ddk import appinfo
import traceback,json
from config import pdd_client_id,pdd_client_secret

def test1():
    req = DdkOrderDetailGet()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))

    req.order_sn = '181116-236494521293864'
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
    {'order_detail_response': {'auth_duo_id': 0,
  'batch_no': '',
  'cps_sign': 'CC1000939_25578619_80c3d6ab8a4d5b1624dc5f3fa40ba9ff',
  'custom_parameters': '',
  'duo_coupon_amount': 0,
  'goods_id': 558132,
  'goods_name': '健美创研【10支装】 植物香氛护手霜300g补水滋润保湿美白防干裂',
  'goods_price': 990,
  'goods_quantity': 1,
  'goods_thumbnail_url': 'http://t00img.yangkeduo.com/goods/images/2018-10-22/e925771ccad5dbcc30f1397769fd69d5.jpeg',
  'group_id': 580236494521293864,
  'match_channel': 0,
  'order_amount': 990,
  'order_create_time': 1542332625,
  'order_group_success_time': 1542332629,
  'order_modify_at': 1543911073,
  'order_pay_time': 1542332629,
  'order_receive_time': 1542600778,
  'order_settle_time': None,
  'order_sn': '181116-236494521293864',
  'order_status': 3,
  'order_status_desc': '审核通过',
  'order_verify_time': 1543911073,
  'pid': '1000939_25578619',
  'point_time': None,
  'promotion_amount': 446,
  'promotion_rate': 450,
  'request_id': '15444260975442285',
  'return_status': 0,
  'type': 0,
  'url_last_generate_time': 1542334241,
  'zs_duo_id': None}}
    '''


if __name__ == '__main__':
    test1()