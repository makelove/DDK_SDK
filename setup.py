# -*- coding: utf-8 -*-
# @Time    : 2018-12-09 11:42
# @Author  : play4fun
# @File    : setup.py
# @Software: PyCharm

"""
setup.py:
"""


from setuptools import setup, find_packages
# print('find_packages:',find_packages())

setup(
    name='ddk',
    version='18.12.19',  # 按日期
    author='play4fun',
    author_email='play4fun@foxmail.com',
    packages=find_packages(),
    # packages=['jd_union'],
    install_requires=[],
    license='MIT',
    description="拼多多-多多客联盟 CPS 工具包",
    long_description_content_type="text/markdown",
    long_description='拼多多-多多客联盟 sdk,进行导购推广,有了它，不需要去写爬虫抓取联盟商品信息'
)
