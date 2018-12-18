# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 14:41
# @Author  : play4fun
# @File    : 多多客工具生成转盘抽免单url1.py
# @Software: PyCharm

"""
多多客工具生成转盘抽免单url1.py:
gw-api.pinduoduo.com/api/router?data_type=JSON&client_id=1350fc17ca6f4b0085db1b53cdb461ef&version=V1&timestamp=1545117029&type=pdd.ddk.lottery.url
.gen&sign=9ECA077875A13E55C804805F8F107473&pid_list=%5B%221000939_25578619%22%5D
"""

from ddk.api.rest.DdkLotteryUrlGen import DdkLotteryUrlGen
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret, pid


def test1():
    req = DdkLotteryUrlGen()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))

    req.pid_list = f'["{pid}"]'

    try:
        resp = req.getResponse()#TODO 参数错误:您无权使用该接口
        print(resp)
        print('-' * 40)
        print(json.dumps(resp))

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())


if __name__ == '__main__':
    test1()
