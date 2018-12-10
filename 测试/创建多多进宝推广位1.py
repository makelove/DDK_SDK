# -*- coding: utf-8 -*-
# @Time    : 2018-12-10 15:29
# @Author  : play4fun
# @File    : 创建多多进宝推广位1.py
# @Software: PyCharm

"""
创建多多进宝推广位1.py:
"""

from ddk.api.rest.DdkGoodsPidGenerate import DdkGoodsPidGenerate
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret


def test1():
    req = DdkGoodsPidGenerate()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))

    req.number = 2
    req.p_id_name_list = ['推广位1', '推广位2']
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
    {'p_id_generate_response': {'p_id_list': [
        {'create_time': 1544427170,
        'p_id': '1000939_44317601',
        'pid_name': '推广位1'},
        
       {'create_time': 1544427170,
        'p_id': '1000939_44317602',
        'pid_name': '推广位2'}
    ],
  'request_id': '15444271701246078'}}
    '''


if __name__ == '__main__':
    test1()
