# -*- coding: utf-8 -*-
# @Time    : 2018-12-10 14:25
# @Author  : play4fun
# @File    : 同步推广订单列表1.py
# @Software: PyCharm

"""
同步推广订单列表1.py:
"""

from ddk.api.rest.DdkOrderListIncrementGet import DdkOrderListIncrementGet
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret
from datetime import datetime, timedelta


def test1():
    req = DdkOrderListIncrementGet()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))

    # req.start_update_time = 1543903041  #有订单
    # req.end_update_time = 1543988976

    start_update_time = int((datetime.now() - timedelta(days=1)).timestamp())
    req.start_update_time = start_update_time  # 1天前,时间跨度不能超过24小时
    req.end_update_time = int(datetime.now().timestamp())
    # req.return_count = True
    try:
        resp = req.getResponse()
        print(resp)
        print('-' * 40)
        print(json.dumps(resp))

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        # {'error_response': {'error_msg': '时间跨度不能超过24小时', 'sub_msg': '时间跨度不能超过24小时', 'sub_code': None, 'error_code': 50001, 'request_id': '15444234942269219'}}
    '''
    {'order_list_get_response': {'order_list': [{'auth_duo_id': 0,
    'batch_no': '',
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
    'p_id': '1000939_25578619',
    'promotion_amount': 446,
    'promotion_rate': 450,
    'type': 0,
    'verify_time': 1543911073000,
    'zs_duo_id': None}],
  'request_id': '15444251942090810',
  'total_count': 1}}
    '''


if __name__ == '__main__':
    test1()
