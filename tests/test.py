#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 10:21
# @Author  : zhm
# @File    : test.py
# @Software: PyCharm
# @Changed : tianyuningmou

from cntm.time_normalizer import TimeNormalizer # 引入包

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
    res = tn.parse(target=u'下午3点')
    print(res)

if __name__ == "__main__":
    origin_test()
    new_test()