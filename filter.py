#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename filter.py
# filter 学习，打印1000以内素数

def _ord_inter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _ord_inter() #初始序列
    while True:
        n = next(it) #给出序列的第一个素数
        yield n
        it = filter(_not_divisible(n), it) #用新生成的素数给出新的序列

for i in primes():
    if i < 100:
        print(i)
    else:
        break
