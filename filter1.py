#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename filter1.py
# 打印1~100的素数

def is_prime(x):
    divid = filter(lambda i: x % i == 0, range(2, x-1))
    print("x:",x,"range:",range(2,x-1),'divid:',divid,"divid len:",len(divid))
    return len(divid) == 0

print(filter(is_prime, range(2, 12)))
