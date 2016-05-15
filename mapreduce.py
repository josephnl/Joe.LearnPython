#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename mapreduce.py
# Mapreduce学习

def caps(name):
    return name.capitalize()
def lowers(name):
    return name.lower()

print(map(caps, map(lowers,['adam', 'LISA', 'barT'])))


def add(x,y):
    return x + y
red = reduce(add, range(1,11,2))

print(red)
