#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename list.py
# 列表生成式
import os

l = [x * x for x in range(1,11)]
l1 = [x * x for x in range(1,11) if x%2 == 0]
print(l)
print(l1)

l2 = [m + n for m in 'abc' for n in 'xyz']
print(l2)

#print([d for d in os.listdir('.')])

L3 = ['Hello', 'World', 18, 'Apple', None]
L4 = [s for s in L3 if isinstance(s,str)]
print(L4)

def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield(b)
        a, b = b, a + b
        n += 1
    return

for n in fib(10):
    print(n)
