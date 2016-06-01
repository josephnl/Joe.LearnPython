# /usr/bin/Python
# coding=utf-8
# ospath.py

import os,os.path

def VisitDir(arg,dirname,names):
  for filespath in name:
    print(os.path.join(dirname,filespath))

if __name__=="__main__":
    path="/root"
    os.path.walk(path,VisitDir,())


# 运行结果, windows 下面没有walk方法

# Traceback (most recent call last):
#   File "C:\Work\Joseph\deploy\ospath.py", line 13, in <module>
#     os.path.walk(path,VisitDir,())
# AttributeError: module 'ntpath' has no attribute 'walk'
