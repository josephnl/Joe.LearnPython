#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename fact.py
# 递归函数


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))
