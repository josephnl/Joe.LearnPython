#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename filter.py
# filter 学习，打印1000以内素数

def _ord_intr():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

for n in _ord_intr():
    if n < 50:
        f = _not_divisible(n)
        print(f)
    else:
        break

def primes():
    yield 2
    it = _ord_intr() #初始序列
    while True:
        n = next(it) #给出序列的第一个素数
        yield n
        it = filter(_not_divisible(n), it) #用新生成的素数给出新的序列
#
for n in primes():
    if n < 10:
        print(n)
    else:
        break
