# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 14:32
# @Author  : play4fun
# @File    : 生成普通商品推广链接1.py
# @Software: PyCharm

"""
生成普通商品推广链接1.py:
"""

from ddk.api.rest.DdkGoodsPromotionUrlGenerate import DdkGoodsPromotionUrlGenerate
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret, pid


def test1():
    req = DdkGoodsPromotionUrlGenerate()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))

    goods_id = '59649770'  # '608295467'
    req.goods_id_list = f'[{goods_id}]'  #
    req.p_id = pid
    req.generate_short_url = True
    req.multi_group = True
    req.generate_we_app = True

    try:
        resp = req.getResponse()
        print(resp)
        print('-' * 40)
        print(json.dumps(resp, indent=2))

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    '''
    {
    "goods_promotion_url_generate_response": {
        "goods_promotion_url_list": [
            {
                "mobile_url": "https://mobile.yangkeduo.com/app.html?launch_url=duo_coupon_landing.html%3Fgoods_id%3D2478116379%26pid%3D1860931_43746459%26cpsSign%3DCC1860931_43746459_01cb1d6f45ae5bc9d01581525853593e%26duoduo_type%3D3",
                "we_app_info": {
                    "we_app_icon_url": "http://xcxcdn.yangkeduo.com/pdd_logo.png",
                    "user_name": "gh_0e7477744313@app",
                    "page_path": "pages/welfare_coupon/welfare_coupon?goods_id=2478116379&pid=1860931_43746459&cpsSign=CC1860931_43746459_01cb1d6f45ae5bc9d01581525853593e&duoduo_type=3",
                    "banner_url": null,
                    "source_display_name": "拼多多",
                    "title": "【劲爆价】210g正品三金西瓜霜经典护龈牙膏 家庭装薄荷香型",
                    "app_id": "wx32540bd863b27570",
                    "desc": "拼多多，多实惠，多乐趣。"
                },
                "mobile_short_url": "https://p.pinduoduo.com/ctzmcX8k",
                "we_app_web_view_url": "https://mobile.yangkeduo.com/duo_coupon_landing.html?goods_id=2478116379&pid=1860931_43746459&cpsSign=CC1860931_43746459_01cb1d6f45ae5bc9d01581525853593e&duoduo_type=3&launch_wx=1",
                "goods_detail": {
                    "avg_desc": 473,
                    "category_name": "海淘",
                    "coupon_remain_quantity": 19000,
                    "avg_serv": 475,
                    "avg_lgst": 474,
                    "serv_pct": 0.3734,
                    "promotion_rate": 400,
                    "sold_quantity": 531,
                    "cat_ids": [
                        17285,
                        17286,
                        17325,
                        0
                    ],
                    "coupon_min_order_amount": 300,
                    "lgst_pct": 0.38,
                    "category_id": 12,
                    "mall_id": 1590059,
                    "goods_eval_score": 4.69,
                    "cat_id": null,
                    "mall_name": "名康家居馆",
                    "coupon_total_quantity": 20000,
                    "desc_pct": 0.4086,
                    "merchant_type": 1,
                    "goods_name": "【劲爆价】210g正品三金西瓜霜经典护龈牙膏 家庭装薄荷香型",
                    "goods_eval_count": 55,
                    "goods_id": 2478116379,
                    "goods_gallery_urls": [
                        "http://t00img.yangkeduo.com/goods/images/2018-08-01/b4f0ca07bcba9486b501944049d2d1a3.jpeg",
                        "http://t00img.yangkeduo.com/goods/images/2018-08-01/408dc0b261e6a7c0e2c5ace66ccd3987.jpeg",
                        "http://t00img.yangkeduo.com/goods/images/2018-08-01/38648c2a3c8124db97afbfacce87235d.jpeg",
                        "http://t00img.yangkeduo.com/goods/images/2018-08-01/2a4ae46491e62bb10e215a57ad3efd43.jpeg",
                        "http://t00img.yangkeduo.com/goods/images/2018-08-01/43f4ba6c94ce9e0e1b281c9cc731ae41.jpeg"
                    ],
                    "goods_desc": "【劲爆价】210g正品三金西瓜霜经典护龈牙膏 家庭装薄荷香型\n厂家正品",
                    "opt_name": "海淘",
                    "goods_thumbnail_url": "http://t00img.yangkeduo.com/goods/images/2018-08-04/b40c7bad375943d178de8c87ee806cee.jpeg",
                    "opt_id": 12,
                    "opt_ids": [
                        292,
                        293,
                        328,
                        923,
                        12,
                        223,
                        15
                    ],
                    "goods_image_url": "http://t00img.yangkeduo.com/goods/images/2018-08-01/52d8afe92e28104f3ac03fbf917a78f8.jpeg",
                    "min_normal_price": 1990,
                    "has_coupon": true,
                    "mall_rate": 100,
                    "create_at": 1533372520,
                    "min_group_price": 990,
                    "mall_cps": 1,
                    "coupon_start_time": 1543766400,
                    "coupon_discount": 300,
                    "coupon_end_time": 1546271999
                },
                "url": "https://mobile.yangkeduo.com/duo_coupon_landing.html?goods_id=2478116379&pid=1860931_43746459&cpsSign=CC1860931_43746459_01cb1d6f45ae5bc9d01581525853593e&duoduo_type=3",
                "short_url": "https://p.pinduoduo.com/svsmce9Z",
                "we_app_web_view_short_url": "https://p.pinduoduo.com/ranmyGCa"
            }
        ],
        "request_id": "15443375918044319"
    }
}
    '''


if __name__ == '__main__':
    test1()
