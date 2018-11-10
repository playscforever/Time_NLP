#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 10:21
# @Author  : zhm
# @File    : test.py
# @Software: PyCharm
# @Changed : tianyuningmou
import re
from cntm.time_normalizer import TimeNormalizer  # 引入包
from datetime import datetime

tn = TimeNormalizer()


def origin_test():
    res = tn.parse(target=u'我需要大概33天2分钟四秒', timeBase='2013-02-28 16:30:29')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)


def test_time_base():
    print(tn.parse(target='今天上午9点叫我', timeBase='2018-11-10 00:07:21'))
    print(tn.parse(target='上午9点叫我', timeBase='2018-11-10 00:07:21'))
    print(tn.parse(target='9点叫我', timeBase='2018-11-10 00:07:21'))

def new_a_moment():
    res = tn.parse(target=u'过一会')
    print(type(res['timedelta']))
    print(res)
    print(datetime.now() + res['timedelta'])


def test_half():
    print(tn.parse(target='半个小时后'))
    print(tn.parse(target='两个半个小时后'))
    print(tn.parse(target='过一会'))
    print(datetime.now() + tn.parse(target='两个半个小时后')['timedelta'])


if __name__ == "__main__":
    test_time_base()
