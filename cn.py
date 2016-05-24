# /usr/bin/python
# encoding: utf-8

所有 = all
class 男人:
    @classmethod
    def 包括(cls,ta):
        return isinstance(ta,cls)

def 一起玩(人们):
    if 所有(男人.包括(ta) for ta in 人们):
        print("他们是基友")
    else:
        print("他们是朋友")
汤姆 = 男人()
杰瑞 = 男人()

一起玩([汤姆,杰瑞])
