# -*- coding: utf-8 -*-
# @Time    : 2018-12-10 15:45
# @Author  : play4fun
# @File    : 生成红包推广链接1.py
# @Software: PyCharm

"""
生成红包推广链接1.py:
"""


from ddk.api.rest.DdkRpPromUrlGenerate import DdkRpPromUrlGenerate
from ddk import appinfo
import traceback,json
from config import pdd_client_id,pdd_client_secret

def test1():
    req = DdkRpPromUrlGenerate()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))

    req.p_id_list = '["1860931_44317832","1860931_44317831"]'
    req.generate_short_url = True
    req.generate_we_app = True
    req.we_app_web_view_short_url = True
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
    {'rp_promotion_url_generate_response': {'request_id': '15444280836807780',
  'url_list': [{'mobile_short_url': 'https://p.pinduoduo.com/TY7mctJv',
    'mobile_url': 'https://mobile.yangkeduo.com/app.html?launch_url=duo_red_packet.html%3Fpid%3D1860931_44317832%26cpsSign%3DCR1860931_44317832_04e872d20ecfcb932048c209616a0096%26duoduo_type%3D2',
    'multi_group_mobile_short_url': 'https://p.pinduoduo.com/y5SmygVa',
    'multi_group_mobile_url': 'https://mobile.yangkeduo.com/app.html?launch_url=duo_red_packet.html%3Fpid%3D1860931_44317832%26cpsSign%3DCR1860931_44317832_04e872d20ecfcb932048c209616a0096%26duoduo_type%3D3',
    'multi_group_short_url': 'https://p.pinduoduo.com/WJgmchVm',
    'multi_group_url': 'https://mobile.yangkeduo.com/duo_red_packet.html?pid=1860931_44317832&cpsSign=CR1860931_44317832_04e872d20ecfcb932048c209616a0096&duoduo_type=3',
    'multi_we_app_web_view_short_url': 'https://p.pinduoduo.com/y5SmygVa',
    'multi_we_app_web_view_url': 'https://mobile.yangkeduo.com/duo_red_packet.html?pid=1860931_44317832&cpsSign=CR1860931_44317832_04e872d20ecfcb932048c209616a0096&duoduo_type=3&launch_wx=1',
    'short_url': 'https://p.pinduoduo.com/TqpmyxD9',
    'url': 'https://mobile.yangkeduo.com/duo_red_packet.html?pid=1860931_44317832&cpsSign=CR1860931_44317832_04e872d20ecfcb932048c209616a0096&duoduo_type=2',
    'we_app_info': {'app_id': 'wx32540bd863b27570',
     'banner_url': None,
     'desc': '拼多多，多实惠，多乐趣。',
     'page_path': 'package_b/duoduo_envelope/duoduo_envelope?pid=1860931_44317832&cpsSign=CR1860931_44317832_04e872d20ecfcb932048c209616a0096&duoduo_type=2',
     'source_display_name': '拼多多',
     'title': '送你个红包，快来领吧',
     'user_name': 'gh_0e7477744313@app',
     'we_app_icon_url': 'http://xcxcdn.yangkeduo.com/pdd_logo.png'},
    'we_app_web_view_short_url': 'https://p.pinduoduo.com/APqmF4yp',
    'we_app_web_view_url': 'https://mobile.yangkeduo.com/duo_red_packet.html?pid=1860931_44317832&cpsSign=CR1860931_44317832_04e872d20ecfcb932048c209616a0096&duoduo_type=2&launch_wx=1'},
   {'mobile_short_url': 'https://p.pinduoduo.com/ALVmclZj',
    'mobile_url': 'https://mobile.yangkeduo.com/app.html?launch_url=duo_red_packet.html%3Fpid%3D1860931_44317831%26cpsSign%3DCR1860931_44317831_92b7c4eea1f4b82c7dbcfa106ce2396a%26duoduo_type%3D2',
    'multi_group_mobile_short_url': 'https://p.pinduoduo.com/4dSmcEYW',
    'multi_group_mobile_url': 'https://mobile.yangkeduo.com/app.html?launch_url=duo_red_packet.html%3Fpid%3D1860931_44317831%26cpsSign%3DCR1860931_44317831_92b7c4eea1f4b82c7dbcfa106ce2396a%26duoduo_type%3D3',
    'multi_group_short_url': 'https://p.pinduoduo.com/lssmy0cZ',
    'multi_group_url': 'https://mobile.yangkeduo.com/duo_red_packet.html?pid=1860931_44317831&cpsSign=CR1860931_44317831_92b7c4eea1f4b82c7dbcfa106ce2396a&duoduo_type=3',
    'multi_we_app_web_view_short_url': 'https://p.pinduoduo.com/4dSmcEYW',
    'multi_we_app_web_view_url': 'https://mobile.yangkeduo.com/duo_red_packet.html?pid=1860931_44317831&cpsSign=CR1860931_44317831_92b7c4eea1f4b82c7dbcfa106ce2396a&duoduo_type=3&launch_wx=1',
    'short_url': 'https://p.pinduoduo.com/Xmmmc90U',
    'url': 'https://mobile.yangkeduo.com/duo_red_packet.html?pid=1860931_44317831&cpsSign=CR1860931_44317831_92b7c4eea1f4b82c7dbcfa106ce2396a&duoduo_type=2',
    'we_app_info': {'app_id': 'wx32540bd863b27570',
     'banner_url': None,
     'desc': '拼多多，多实惠，多乐趣。',
     'page_path': 'package_b/duoduo_envelope/duoduo_envelope?pid=1860931_44317831&cpsSign=CR1860931_44317831_92b7c4eea1f4b82c7dbcfa106ce2396a&duoduo_type=2',
     'source_display_name': '拼多多',
     'title': '送你个红包，快来领吧',
     'user_name': 'gh_0e7477744313@app',
     'we_app_icon_url': 'http://xcxcdn.yangkeduo.com/pdd_logo.png'},
    'we_app_web_view_short_url': 'https://p.pinduoduo.com/crUmyp2G',
    'we_app_web_view_url': 'https://mobile.yangkeduo.com/duo_red_packet.html?pid=1860931_44317831&cpsSign=CR1860931_44317831_92b7c4eea1f4b82c7dbcfa106ce2396a&duoduo_type=2&launch_wx=1'}]}}
    '''

if __name__ == '__main__':
    test1()