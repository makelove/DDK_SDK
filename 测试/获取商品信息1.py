# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 13:01
# @Author  : play4fun
# @File    : 获取商品信息1.py
# @Software: PyCharm

"""
获取商品信息1.py:


promotion_rate 佣金比例，千分比
佣金=成交价x佣金比例/1000 单位为分

min_group_price 最低价sku的拼团价，单位为分
min_normal_price 最低价sku的单买价，单位为分

转链后
https://mobile.yangkeduo.com/duo_coupon_landing.html?goods_id=344663340973&pid=1860931_197796447&goods_sign=E9j28lXHyTlGSjrVwvfa_LAGVflKJo_x_JQxaEVdW6j&zs_duo_id=25436963&cpsSign=CC_220511_1860931_197796447_5a031f10071b56bebb28fcc1a4fdcfdb&_x_ddjb_act=%7B%22st%22%3A%221%22%7D&duoduo_type=2

https://blog.csdn.net/glorious_future/article/details/114996411
通过搜索接口，搜索接口的keyword是支持传goods_id的，返回来的商品详情是带着goods_sign的，这样我们就拿到了goods_sign了


"""

from ddk.api.rest.DdkGoodsDetail import DdkGoodsDetail
from ddk import appinfo
import traceback
import json
from config import pdd_client_id, pdd_client_secret
from pprint import pprint


def test1():
    req = DdkGoodsDetail()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))

    # 过时
    # goods_id='4532814226,2478116379'#参数错误:只支持单个goodsId查询
    # goods_id = '73224807'  # '608295467'

    sign = 'E9j28lXHyTlGSjrVwvfa_LAGVflKJo_x_JQxaEVdW6j'
    # sign = 'C4KXLHYA6AXF5RAWR3MOKHALRE_GEXDA'
    req.goods_sign = sign  # OK
    try:
        resp = req.getResponse()
        pprint(resp)

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    '''
    {'goods_detail_response': {'goods_details': 
    [{'cat_ids': [8172, 8181, 8226],
      'category_id': 10696,
      'category_name': '海淘',
      'coupon_discount': 400,
      'coupon_end_time': 1617465599,
      'coupon_min_order_amount': 400,
      'coupon_remain_quantity': 42000,
      'coupon_start_time': 1617120000,
      'coupon_total_quantity': 50000,
      'desc_txt': '高',
      'goods_desc': '云南板栗贝贝南瓜10斤板栗味贝贝小南瓜宝宝辅食老南瓜10/5/3斤',
      'goods_gallery_urls': ['https://img.pddpic.com/mms-material-img/2021-03-18/02a2f2ba-4c20-4e72-9fe0-c8ed2470c7a0.jpeg.a.jpeg',
                             'https://img.pddpic.com/mms-material-img/2021-03-04/07fa2be2-adf7-45a2-a77c-0303cf25f8bd.jpeg.a.jpeg',
                             'https://img.pddpic.com/mms-material-img/2021-03-04/77c71f19-80e7-42e7-a18d-ec097c92015d.jpeg.a.jpeg',
                             'https://img.pddpic.com/mms-material-img/2021-03-04/3f37b98a-f808-4cb7-9882-06563462ffb5.jpeg.a.jpeg',
                             'https://img.pddpic.com/mms-material-img/2021-03-07/068932ec-8c67-43eb-9447-d6314ca755f3.jpeg.a.jpeg',
                             'https://img.pddpic.com/mms-material-img/2021-03-07/477b41ce-908d-413c-9eab-f821b7a06526.jpeg.a.jpeg',
                             'https://img.pddpic.com/mms-material-img/2021-03-07/101a13a1-61d8-451f-84db-b71603d12dec.jpeg.a.jpeg',
                             'https://img.pddpic.com/mms-material-img/2021-03-04/174e9343-b6d0-4f8c-b7f8-ce7909f070eb.jpeg.a.jpeg',
                             'https://img.pddpic.com/mms-material-img/2021-03-04/8e7cb92b-866c-4959-a416-ad2d0d12dc77.jpeg.a.jpeg',
                             'https://img.pddpic.com/mms-material-img/2021-03-04/b52dda59-71d5-40d4-b0af-1c79a6e77994.jpeg.a.jpeg'],
      'goods_id': 222575613798,
      'goods_image_url': 'https://img.pddpic.com/mms-material-img/2021-03-18/02a2f2ba-4c20-4e72-9fe0-c8ed2470c7a0.jpeg.a.jpeg',
      'goods_name': '云南板栗贝贝南瓜10斤板栗味贝贝小南瓜宝宝辅食老南瓜10/5/3斤',
      'goods_sign': 'Y9X2kbjEqfJGSjrVwvfZUTm_mDXRAAKI_JQFsEOOZIj',
      'goods_thumbnail_url': 'https://t00img.yangkeduo.com/goods/images/2021-03-18/ac0c94338b83d5b1c5cfc493078b8b20.jpeg',
      'has_coupon': True,
      'has_mall_coupon': False,
      'lgst_txt': '高',
      'mall_coupon_discount_pct': 0,
      'mall_coupon_end_time': 0,
      'mall_coupon_max_discount_amount': 0,
      'mall_coupon_min_order_amount': 0,
      'mall_coupon_remain_quantity': 0,
      'mall_coupon_start_time': 0,
      'mall_coupon_total_quantity': 0,
      'mall_cps': 1,
      'mall_id': 891464,
      'mall_img_url': 'http://t16img.yangkeduo.com/pdd_ims/57951b6a06f626cac503643340156880.jpg',
      'mall_name': '哈尼印象',
      'merchant_type': 1,
      'min_group_price': 990,
      'min_normal_price': 1590,
      'only_scene_auth': True,
      'opt_id': 10696,
      'opt_ids': [10723, 22884, 10696, 22280, 22281, 22921, 9419, 9451, 10700, 13, 9421, 12402, 8115, 151, 22879],
      'opt_name': '海淘',
      'plan_type': 4,
      'predict_promotion_rate': 140,
      'promotion_rate': 140,
      'sales_tip': '6967',
      'serv_txt': '高',
      'service_tags': [9, 13],
      'share_rate': 0,
      'unified_tags': ['坏了包赔',
                       '48小时发货'],
      'video_urls': [],
      'zs_duo_id': 8439561}],
    'request_id': '16172464391342144'}}


    '''


if __name__ == '__main__':
    test1()
