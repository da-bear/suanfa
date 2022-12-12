"""
有个非负整数，将其按照字符串拼接的方式拼接为一个整数。
如何拼接可以使得得到的整数最大？
例：32,94,128,1286,6,71
"""
from functools import cmp_to_key
# 多字段排序

lst = [32, 94, 128, 1286, 6, 71]


def xy_cmp(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def number_join(li):
    li = list(map(str, li))
    li.sort(key=cmp_to_key(xy_cmp))
    return "".join(li)


print(number_join(lst))
