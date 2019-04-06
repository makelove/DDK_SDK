# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 13:01
# @Author  : play4fun
# @File    : 获取商品信息1.py
# @Software: PyCharm

"""
获取商品信息1.py:
"""

from ddk.api.rest.DdkGoodsDetail import DdkGoodsDetail
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret


def test1():
    req = DdkGoodsDetail()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    # goods_id='4532814226,2478116379'#参数错误:只支持单个goodsId查询
    goods_id = '1695213'  # '608295467'
    req.goods_id_list = f'[{goods_id}]'  #
    try:
        resp = req.getResponse()
        print(resp)

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    '''
    {'goods_detail_response': {'goods_details': [{'avg_desc': 473,
    'avg_lgst': 474,
    'avg_serv': 475,
    'cat_id': None,
    'cat_ids': [17285, 17286, 17325, 0],
    'category_id': 12,
    'category_name': '海淘',
    'coupon_discount': 300,
    'coupon_end_time': 1546271999,
    'coupon_min_order_amount': 300,
    'coupon_remain_quantity': 19000,
    'coupon_start_time': 1543766400,
    'coupon_total_quantity': 20000,
    'create_at': 1533372520,
    'desc_pct': 0.4086,
    'goods_desc': '【劲爆价】210g正品三金西瓜霜经典护龈牙膏 家庭装薄荷香型\n厂家正品',
    'goods_eval_count': 55,
    'goods_eval_score': 4.69,
    'goods_gallery_urls': ['http://t00img.yangkeduo.com/goods/images/2018-08-01/b4f0ca07bcba9486b501944049d2d1a3.jpeg',
     'http://t00img.yangkeduo.com/goods/images/2018-08-01/408dc0b261e6a7c0e2c5ace66ccd3987.jpeg',
     'http://t00img.yangkeduo.com/goods/images/2018-08-01/38648c2a3c8124db97afbfacce87235d.jpeg',
     'http://t00img.yangkeduo.com/goods/images/2018-08-01/2a4ae46491e62bb10e215a57ad3efd43.jpeg',
     'http://t00img.yangkeduo.com/goods/images/2018-08-01/43f4ba6c94ce9e0e1b281c9cc731ae41.jpeg'],
    'goods_id': 2478116379,
    'goods_image_url': 'http://t00img.yangkeduo.com/goods/images/2018-08-01/52d8afe92e28104f3ac03fbf917a78f8.jpeg',
    'goods_name': '【劲爆价】210g正品三金西瓜霜经典护龈牙膏 家庭装薄荷香型',
    'goods_thumbnail_url': 'http://t00img.yangkeduo.com/goods/images/2018-08-04/b40c7bad375943d178de8c87ee806cee.jpeg',
    'has_coupon': True,
    'lgst_pct': 0.38,
    'mall_cps': 1,
    'mall_id': 1590059,
    'mall_name': '名康家居馆',
    'mall_rate': 100,
    'merchant_type': 1,
    'min_group_price': 990,
    'min_normal_price': 1990,
    'opt_id': 12,
    'opt_ids': [292, 293, 328, 923, 12, 223, 15],
    'opt_name': '海淘',
    'promotion_rate': 400,
    'serv_pct': 0.3734,
    'sold_quantity': 503}],
  'request_id': '15443329840343061'}}
    '''


if __name__ == '__main__':
    test1()
