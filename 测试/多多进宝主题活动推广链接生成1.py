# -*- coding: utf-8 -*-
# @Time    : 2018-12-18 17:43
# @Author  : play4fun
# @File    : 多多进宝主题活动推广链接生成1.py
# @Software: PyCharm

"""
多多进宝主题活动推广链接生成1.py:

DdkThemePromUrlGenerate

"""

from ddk.api.rest.DdkThemePromUrlGenerate import DdkThemePromUrlGenerate
from ddk import appinfo
import traceback, json
from config import pdd_client_id, pdd_client_secret, pid


def test1():
    req = DdkThemePromUrlGenerate()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    #
    req.pid = pid
    req.theme_id_list = [3925, 3975]
    req.generate_short_url = True
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
    "theme_promotion_url_generate_response": {
        "url_list": [
            {
                "multi_we_app_web_view_url": "https://mobile.yangkeduo.com/duo_theme_activity.html?themeId=3925&pid=1860931_43746459&cpsSign=CT1860931_43746459_55b94304f7ead939318bad121c195dac&duoduo_type=3&launch_wx=1",
                "multi_group_mobile_short_url": null,
                "mobile_url": null,
                "multi_we_app_web_view_short_url": null,
                "multi_group_mobile_url": null,
                "url": "https://mobile.yangkeduo.com/duo_theme_activity.html?themeId=3925&pid=1860931_43746459&cpsSign=CT1860931_43746459_55b94304f7ead939318bad121c195dac&duoduo_type=2",
                "short_url": "https://p.pinduoduo.com/ATomTqec",
                "multi_group_url": "https://mobile.yangkeduo.com/duo_theme_activity.html?themeId=3925&pid=1860931_43746459&cpsSign=CT1860931_43746459_55b94304f7ead939318bad121c195dac&duoduo_type=3",
                "multi_group_short_url": "https://p.pinduoduo.com/QdKmFl8h",
                "we_app_info": null,
                "mobile_short_url": null,
                "we_app_web_view_url": "https://mobile.yangkeduo.com/duo_theme_activity.html?themeId=3925&pid=1860931_43746459&cpsSign=CT1860931_43746459_55b94304f7ead939318bad121c195dac&duoduo_type=2&launch_wx=1",
                "we_app_web_view_short_url": "https://p.pinduoduo.com/OoymcRVm"
            },
            {
                "multi_we_app_web_view_url": "https://mobile.yangkeduo.com/duo_theme_activity.html?themeId=3975&pid=1860931_43746459&cpsSign=CT1860931_43746459_55b94304f7ead939318bad121c195dac&duoduo_type=3&launch_wx=1",
                "multi_group_mobile_short_url": null,
                "mobile_url": null,
                "multi_we_app_web_view_short_url": null,
                "multi_group_mobile_url": null,
                "url": "https://mobile.yangkeduo.com/duo_theme_activity.html?themeId=3975&pid=1860931_43746459&cpsSign=CT1860931_43746459_55b94304f7ead939318bad121c195dac&duoduo_type=2",
                "short_url": "https://p.pinduoduo.com/1PBmFAaX",
                "multi_group_url": "https://mobile.yangkeduo.com/duo_theme_activity.html?themeId=3975&pid=1860931_43746459&cpsSign=CT1860931_43746459_55b94304f7ead939318bad121c195dac&duoduo_type=3",
                "multi_group_short_url": "https://p.pinduoduo.com/jX3mFH36",
                "we_app_info": null,
                "mobile_short_url": null,
                "we_app_web_view_url": "https://mobile.yangkeduo.com/duo_theme_activity.html?themeId=3975&pid=1860931_43746459&cpsSign=CT1860931_43746459_55b94304f7ead939318bad121c195dac&duoduo_type=2&launch_wx=1",
                "we_app_web_view_short_url": "https://p.pinduoduo.com/VJLmFGH8"
            }
        ],
        "request_id": "15451265248810004"
    }
}
    '''


if __name__ == '__main__':
    test1()
