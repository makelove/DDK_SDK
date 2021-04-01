# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 14:02
# @Author  : play4fun
# @File    : DdkGoodsSearch.py
# @Software: PyCharm

"""
DdkGoodsSearch.py:

2021

https://jinbao.pinduoduo.com/third-party/api-detail?apiName=pdd.ddk.goods.search
多多进宝商品查询


https://jinbao.pinduoduo.com/qa-system?questionId=219
授权备案成功后，为何pdd.ddk.goods.search接口还是返回未备案报错？
仔细检查一下pdd.ddk.goods.search传入的pid+custom_parameters和生成备案链接的入参pid+custom_parameters是否一致，可能是pid漏传或者custom_parameters漏传了。

"""

from ddk.api.base import RestApi


class DdkGoodsSearch(RestApi):
    def __init__(self, domain='gw-api.pinduoduo.com', port=80):
        RestApi.__init__(self, domain, port)
        self.keyword = None  # 商品关键词，与opt_id字段选填一个或全部填写

        self.page_size = None  # 默认100，每页商品数量
        self.sort_type = None  # 排序方式:0-综合排序;1-按佣金比率升序;2-按佣金比例降序;3-按价格升序;4-按价格降序;5-按销量升序;6-按销量降序;7-优惠券金额排序升序;8-优惠券金额排序降序;9-券后价升序排序;10-券后价降序排序;11-按照加入多多进宝时间升序;12-按照加入多多进宝时间降序;13-按佣金金额升序排序;14-按佣金金额降序排序;15-店铺描述评分升序;16-店铺描述评分降序;17-店铺物流评分升序;18-店铺物流评分降序;19-店铺服务评分升序;20-店铺服务评分降序;27-描述评分击败同类店铺百分比升序，28-描述评分击败同类店铺百分比降序，29-物流评分击败同类店铺百分比升序，30-物流评分击败同类店铺百分比降序，31-服务评分击败同类店铺百分比升序，32-服务评分击败同类店铺百分比降序
        self.with_coupon = None  # false返回所有商品，true只返回有优惠券的商品
        self.range_list = None  #
        self.cat_id = None  # 商品类目ID，使用pdd.goods.cats.get接口获取
        self.goods_id_list = None  # 商品ID列表。例如：[123456,123]，当入参带有goods_id_list字段，将不会以opt_id、 cat_id、keyword维度筛选商品
        self.zs_duo_id = None  # 招商多多客ID
        self.merchant_type = None  # 店铺类型，1-个人，2-企业，3-旗舰店，4-专卖店，5-专营店，6-普通店（未传为全部）

        self.pid = None  # 推广位id
        self.custom_parameters = None  # 自定义参数

    def getapiname(self):
        return 'pdd.ddk.goods.search'
