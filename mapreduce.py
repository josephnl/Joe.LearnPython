#/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename mapreduce.py
# Mapreduce学习


def caps(name):
    return name.capitalize()
def lowers(name):
    return name.lower()

l = list(map(caps, map(lowers,['adam', 'LISA', 'barT'])))
print(l)


from functools import reduce
def add(x,y):
    return x + y
print(reduce(add, range(1,11,2)))
