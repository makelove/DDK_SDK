# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 16:02
# @Author  : play4fun
# @File    : 获取拼多多标准商品类目信息1.py
# @Software: PyCharm

"""
获取拼多多标准商品类目信息1.py:

GoodsCatsGet
"""

from ddk.api.rest.GoodsCatsGet import GoodsCatsGet
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret


def test1():
    req = GoodsCatsGet()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    #
    req.parent_cat_id = 5851#电脑 #259#"饰品首饰"

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
    "goods_cats_get_response": {
        "goods_cats_list": [
            {
                "level": 1,
                "cat_name": "美容护肤/精油",
                "cat_id": 69,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "男装",
                "cat_id": 239,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "饰品首饰",
                "cat_id": 259,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "厨房用品",
                "cat_id": 282,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "家庭清洁",
                "cat_id": 479,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "洗护纸品",
                "cat_id": 483,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "居家日用",
                "cat_id": 489,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "收纳整理",
                "cat_id": 519,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "宠物用品",
                "cat_id": 525,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "珠宝黄金",
                "cat_id": 1166,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "个护美体",
                "cat_id": 1432,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "彩妆/香水/美妆工具",
                "cat_id": 1464,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "成人用品",
                "cat_id": 1715,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "鲜花园艺",
                "cat_id": 1889,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "办公用品",
                "cat_id": 2603,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "文化用品",
                "cat_id": 2629,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "3C数码配件",
                "cat_id": 2933,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "书籍杂志",
                "cat_id": 3202,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "乐器/吉他/钢琴/配件",
                "cat_id": 4958,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "影音电器",
                "cat_id": 5752,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "手机",
                "cat_id": 5834,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "二手数码",
                "cat_id": 5839,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "电脑",
                "cat_id": 5851,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "数码相机/单反相机/摄像机",
                "cat_id": 5906,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "智能设备",
                "cat_id": 5921,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "厨房电器",
                "cat_id": 5955,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "大家电",
                "cat_id": 6076,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "生活电器",
                "cat_id": 6128,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "个人护理保健",
                "cat_id": 6209,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "网络设备",
                "cat_id": 6290,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "零食/坚果/特产",
                "cat_id": 6398,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "咖啡/麦片/冲饮",
                "cat_id": 6536,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "茶",
                "cat_id": 6586,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "粮油米面/南北干货/调味品",
                "cat_id": 6630,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "酒类",
                "cat_id": 6758,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "保健食品/膳食营养补充食品",
                "cat_id": 6785,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "传统滋补品",
                "cat_id": 6883,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "电子元器件市场",
                "cat_id": 7323,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "摩托车/装备/配件",
                "cat_id": 7629,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "汽车/用品/配件/改装",
                "cat_id": 7639,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "水产肉类/新鲜蔬果/熟食",
                "cat_id": 8172,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "女装/女士精品",
                "cat_id": 8439,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "新车/二手车",
                "cat_id": 8502,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "流行男鞋",
                "cat_id": 8508,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "女鞋",
                "cat_id": 8509,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "箱包皮具/女包/男包",
                "cat_id": 8538,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "内衣裤袜",
                "cat_id": 8583,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "腕表眼镜",
                "cat_id": 8634,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "服饰配件",
                "cat_id": 8669,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "本地化生活服务",
                "cat_id": 8721,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "电影/演出/体育赛事",
                "cat_id": 8722,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "个性定制/设计服务",
                "cat_id": 8723,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "购物卡/礼品卡/代金券",
                "cat_id": 8724,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "婚庆/摄影/摄像服务",
                "cat_id": 8725,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "教育培训",
                "cat_id": 8726,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "景点门票/周边游",
                "cat_id": 8727,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "旅游路线/商品/服务",
                "cat_id": 8728,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "生活缴费",
                "cat_id": 8729,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "影视/会员/腾讯QQ专区",
                "cat_id": 8730,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "网络服务/软件",
                "cat_id": 8732,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "网上营业厅",
                "cat_id": 8733,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "休闲娱乐",
                "cat_id": 8734,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "游戏服务/直播",
                "cat_id": 8736,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "床上用品",
                "cat_id": 9313,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "电子/电工",
                "cat_id": 9314,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "基础建材",
                "cat_id": 9315,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "家居饰品",
                "cat_id": 9316,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "家装灯饰光源",
                "cat_id": 9317,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "家装主材",
                "cat_id": 9318,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "居家布艺",
                "cat_id": 9319,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "全屋定制",
                "cat_id": 9320,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "商业/办公家具",
                "cat_id": 9321,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "特色手工艺",
                "cat_id": 9322,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "五金工具",
                "cat_id": 9323,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "住宅家具",
                "cat_id": 9324,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "电动车/配件/交通工具",
                "cat_id": 11683,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "户外/登山/旅行野营用品",
                "cat_id": 11684,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "运动/瑜伽/健身/球类",
                "cat_id": 11685,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "运动包/户外包/配件",
                "cat_id": 11686,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "运动服/休闲服",
                "cat_id": 11687,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "运动鞋",
                "cat_id": 11688,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "自行车/骑行装备/零配件",
                "cat_id": 11689,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "OTC药品/医疗器械/计生用品",
                "cat_id": 13176,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "精制中药材",
                "cat_id": 13177,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "隐形眼镜/护理液",
                "cat_id": 13178,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "奶粉/辅食/营养品/零食",
                "cat_id": 14697,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "尿片/洗护/喂哺/推车床",
                "cat_id": 14740,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "童鞋/婴儿鞋/亲子鞋",
                "cat_id": 14933,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "童装/婴儿装/亲子装",
                "cat_id": 14966,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "玩具/童车/益智/积木/模型",
                "cat_id": 15083,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "孕产妇用品/孕妇装/营养",
                "cat_id": 15356,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "书籍/杂志/报纸",
                "cat_id": 15543,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "农机/农具/农膜",
                "cat_id": 16155,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "畜牧/养殖物资",
                "cat_id": 16192,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "农用物资",
                "cat_id": 16209,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "成人用品/情趣用品",
                "cat_id": 16237,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "宠物/宠物食品及用品",
                "cat_id": 16288,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "餐饮具",
                "cat_id": 16548,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "厨房/烹饪用具",
                "cat_id": 16676,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "收纳整理",
                "cat_id": 16794,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "家庭/个人清洁工具",
                "cat_id": 16901,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "居家日用",
                "cat_id": 16989,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "节庆用品/礼品",
                "cat_id": 17134,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "烟品/打火机/瑞士军刀",
                "cat_id": 17249,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "洗护清洁剂/卫生巾/纸/香薰",
                "cat_id": 17285,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "饰品/流行首饰/时尚饰品",
                "cat_id": 17412,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "珠宝/钻石/翡翠/黄金",
                "cat_id": 17455,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "鲜花速递/花卉仿真/绿植园艺",
                "cat_id": 17671,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "乐器/吉他/钢琴/配件",
                "cat_id": 17803,
                "parent_cat_id": 0
            },
            {
                "level": 1,
                "cat_name": "装修设计/施工/监理",
                "cat_id": 18088,
                "parent_cat_id": 0
            }
        ],
        "request_id": "15451203761173134"
    }
}
    '''


if __name__ == '__main__':
    test1()
