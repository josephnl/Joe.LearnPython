#!/usr/bin/Python
# coding=utf-8
# zip.py

# 测试打包压缩功能

import os

destination = "c:\\users\\hdh\\autopep8.zip"
source = "c:\\users\\hdh\\autopep8\*"
zipcommand = '7z a -tzip -r "%s" "%s" ' % (destination, source)


os.system(zipcommand)
