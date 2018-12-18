
from ddk.api.rest.DdkGoodsDetail import DdkGoodsDetail
from ddk import appinfo
import traceback,json
from config import pdd_client_id,pdd_client_secret

def test1():
    req = DdkGoodsDetail()
    req.set_app_info(appinfo(pdd_client_id, secret=pdd_client_secret))
    #
    # goods_id='4532814226,2478116379'#参数错误:只支持单个goodsId查询
    goods_id='2478116379'
    req.goods_id_list = f'[{goods_id}]'#
    try:
        resp = req.getResponse()
        print(resp)
        print('-' * 40)
        print(json.dumps(resp))

        # print(json.dumps(f, ensure_ascii=False))
    except Exception as e:
        print(e)
        print(traceback.format_exc())


if __name__ == '__main__':
    test1()