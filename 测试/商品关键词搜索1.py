# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 14:12
# @Author  : play4fun
# @File    : 商品关键词搜索1.py
# @Software: PyCharm

"""
商品关键词搜索1.py:

2021-4-1 问题
ddk.api.base.DdkException: errorcode=None message=None subcode=60001
submsg=未传入已经授权备案过的相关参数(pid/custom_parameters)，
授权备案说明链接：https://jinbao.pinduoduo.com/qa-system?questionId=204
application_host= service_host=

"""
from pprint import pprint
from ddk.api.rest.DdkGoodsSearch import DdkGoodsSearch
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret


def test1():
    req = DdkGoodsSearch()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    req.keyword = '美食'

    # goods_id='2478116379'
    # req.goods_id_list = f'[{goods_id}]'#会返回这一条，只有1条

    req.page_size = 10

    #TODO
    req.pid = '1860931_129508134'
    req.custom_parameters = '{"uid":"1860931"}' #多多客ID '1860931'

    try:
        resp = req.getResponse()
        pprint(resp)

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    '''
    {'avg_desc': 462,
 'avg_lgst': 466,
 'avg_serv': 467,
 'cat_id': None,
 'cat_ids': [17285, 17297, 17399, 0],
 'category_id': 12,
 'category_name': '海淘',
 'coupon_discount': 100,
 'coupon_end_time': 1544457599,
 'coupon_min_order_amount': 100,
 'coupon_remain_quantity': 8000,
 'coupon_start_time': 1544198400,
 'coupon_total_quantity': 10000,
 'create_at': 1535875398,
 'desc_pct': 0.1459,
 'goods_desc': None,
 'goods_eval_count': 303,
 'goods_eval_score': 4.44,
 'goods_gallery_urls': None,
 'goods_id': 183245942,
 'goods_image_url': 'http://omsproductionimg.yangkeduo.com/images/2017-11-08/e0fe9079e1ba8f4bd1e1eb7b6c27bdfe.jpeg',
 'goods_name': '30包 20包 10包兰奇抽纸300张婴儿家庭本色批发整箱纸巾餐巾纸',
 'goods_thumbnail_url': 'http://t00img.yangkeduo.com/goods/images/2018-11-12/c3609b5326927f699630273b40220046.jpeg',
 'has_coupon': True,
 'lgst_pct': 0.1573,
 'mall_cps': 1,
 'mall_id': 939972,
 'mall_name': '兰奇纸业',
 'mall_rate': 200,
 'merchant_type': 1,
 'min_group_price': 1251,
 'min_normal_price': 1490,
 'opt_id': 12,
 'opt_ids': [292, 293, 357, 330, 12, 364, 223, 15],
 'opt_name': '海淘',
 'promotion_rate': 300,
 'serv_pct': 0.18,
 'sold_quantity': 13375}
    '''


if __name__ == '__main__':
    test1()
