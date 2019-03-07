# -*- coding: utf-8 -*-
# @Time    : 2019-03-07 19:18
# @Author  : play4fun
# @File    : 根据商品ID查询相关商品-商品推荐1.py
# @Software: PyCharm

"""
根据商品ID查询相关商品-商品推荐1.py:
不行！

广西红心木瓜5斤/10斤 单果500g-1000g新鲜水果
https://mobile.yangkeduo.com/goods2.html?goods_id=5905216563
"""
from pprint import pprint
from ddk.api.rest.DdkGoodsSearch import DdkGoodsSearch
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret


def main():
    req = DdkGoodsSearch()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    req.keyword = '【新品推荐】广西红心木瓜5斤/10斤 单果500g-1000g新鲜水果'
    req.page_size = 10
    # goods_id = '5905216563'  #
    # req.goods_id_list = f'[{goods_id}]'  #
    try:
        resp = req.getResponse()
        pprint(resp)#结果都是木瓜

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())


if __name__ == '__main__':
    main()
