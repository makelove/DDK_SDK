# DDK_SDK
## 拼多多-多多客联盟 CPS 工具包

- 其他平台
    - [京东联盟](https://pypi.org/project/jd-union/)
    - [淘宝联盟](https://github.com/makelove/Taobao_topsdk)

- 视频 
    - [淘口令被微信屏蔽了？来看看拼多多的【多多客SDK】开放平台](https://www.bilibili.com/video/BV1QE411J7R7/)
    - [Python编程，写一个【QQ+拼多多】返现程序，在服务器上Docker运行](https://www.bilibili.com/video/BV15E411L7rk/)
    - [【编程】拼多多-多多客-开发者-SDK，多多进宝。Python](https://www.bilibili.com/video/BV1GK4y1m7q8/)

- 官网
    - https://open.pinduoduo.com/#/index
    - 开发者文档
        - [多多客入驻指南](https://open.pinduoduo.com/#/document?title=%25E5%25A4%259A%25E5%25A4%259A%25E5%25AE%25A2%25E5%2585%25A5%25E9%25A9%25BB%25E6%258C%2587%25E5%258D%2597)
            - https://open.pinduoduo.com/#/document
            - 必须！第一步！
                - 6、打开多多进宝页面输入client_id，将其与多多客进行绑定。
                    - 【多多进宝】 现在2021年需要实名认证，下载【多多进宝】App
                - 7、绑定成功后，便可成功获取多多客API权限。
        - 多多客API
            - https://open.pinduoduo.com/#/apidocument
        - 多多客权限包
            - http://open.pinduoduo.com/#/apidocument?port=5&id=2
    - 多多进宝
        - https://jinbao.pinduoduo.com/index

- 常用API
    - [pdd.ddk.goods.detail多多进宝商品详情查询](https://open.pinduoduo.com/application/document/api?id=pdd.ddk.goods.detail&permissionId=2)
        - [GoodsSign接入使用](https://jinbao.pinduoduo.com/qa-system?questionId=252)
    - [多多进宝商品查询：pdd.ddk.goods.search](https://jinbao.pinduoduo.com/third-party/api-detail?apiName=pdd.ddk.goods.search)
    
        

## 注意事项
- 公告
    - [自2021年3月31日起，平台将对长期未发布服务的已上线应用或服务资质进行限制处理](https://open.pinduoduo.com/application/document/announcement?id=159)
    - [授权备案](https://jinbao.pinduoduo.com/qa-system?questionId=204)
        - [如何授权备案？](https://jinbao.pinduoduo.com/qa-system?questionId=218)
        - [查询是否绑定备案：pdd.ddk.member.authority.query](https://jinbao.pinduoduo.com/third-party/api-detail?apiName=pdd.ddk.member.authority.query)
        - [生成营销工具推广链接：pdd.ddk.rp.prom.url.generate](https://jinbao.pinduoduo.com/third-party/api-detail?apiName=pdd.ddk.rp.prom.url.generate)
        
    - [多多进宝APP提现门槛降低至10元通知](https://jinbao.pinduoduo.com/message/detail?crumbs=broadcast&id=9851753)
        - 2021-03-14 17:54:57
        - 下载多多进宝官方APP，推广待提现余额满10元即可提现，无需等待，一键提现推广佣金。


- 开发环境
    - python 3.6
    - 仿照 Taobao_topsdk
    - 安装
        - https://pypi.org/project/ddk/
        - pip install ddk
        - pip install ddk --upgrade
        - 卸载
            - pip uninstall ddk

- 交流
    - 加我微信:sexy8dream
    <img src="http://images7n.dark.net.cn/sexy8dream.jpg" width = "300" height = "300" alt="wechat_account"  />

    - 扫码进群
    <img src="http://images7n.dark.net.cn/cps-union-tb-jd-pdd8.jpg" width = "300" height = "473" alt="wechat_donate"  />
