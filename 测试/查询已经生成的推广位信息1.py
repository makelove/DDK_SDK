# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 14:50
# @Author  : play4fun
# @File    : 查询已经生成的推广位信息1.py
# @Software: PyCharm

"""
查询已经生成的推广位信息1.py:
"""

from ddk.api.rest.DdkGoodsPidQuery import DdkGoodsPidQuery
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret


def test1():
    req = DdkGoodsPidQuery()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))

    req.page_size = 100
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
    "p_id_query_response": {
        "p_id_list": [
            {
                "create_time": 1544024512,
                "pid_name": "推广位1860731_43745459",
                "p_id": "1860731_43745459"
            },
            {
                "create_time": 1532571981,
                "pid_name": "tgw1",
                "p_id": "1860731_21505724"
            }
        ],
        "total_count": 2,
        "request_id": "15443382778507289"
    }
}
    '''

if __name__ == '__main__':
    test1()
