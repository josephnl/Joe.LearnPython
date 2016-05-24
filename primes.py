#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename prime.py
# filter 学习，打印1000以内素数

def main():
    for n in primes():
        if n < 10:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()
