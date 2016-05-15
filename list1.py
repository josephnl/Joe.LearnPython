#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename list1.py
# 读取本目录的文件名并且打包压缩，备份

import os


filename = [d for d in os.listdir('.')]
print(filename)
