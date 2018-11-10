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
    res = tn.parse(target=u'晚上8点到上午10点之间')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target=u'2013年二月二十八日下午四点三十分二十九秒',
                   timeBase='2013-02-28 16:30:29')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target=u'我需要大概33天2分钟四秒', timeBase='2013-02-28 16:30:29')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target=u'今年儿童节晚上九点一刻')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target=u'三日')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target=u'11日')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target=u'7点4')  # target为待分析语句，timeBase为基准时间默认是当前时间
    print(res)

    res = tn.parse(target=u'今年春分')
    print(res)


def new_test():
    # res = tn.parse(target=u'3个半小时后')
    # print(res)
    res = tn.parse(target=u'十分钟后')
    print(type(res['timedelta']))
    print(res)
    print(datetime.now() + res['timedelta'])


def half_repl(m):
    result = 0
    if m.group(1):
        result = int(m.group(1))
    result = result * 60 + 30
    return str(result) + '分钟'


def test_re():
    msg = '2半个小时后'
    msg = re.sub("(\d*)(半个?小时)", half_repl, msg)
    print(msg)

    msg = '半天后'
    msg = re.sub("(\d*)(半个?小时)", half_repl, msg)
    print(msg)
    # res = tn.parse(target=msg)
    # print(res)


if __name__ == "__main__":
    new_test()
    # test_re()
