"""
计算时间
"""

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s func running %s sec" % (func.__name__, (t2 - t1)))
        return result
    return wrapper


# def branch_ft():
#     # test 键盘
#     #xisdlufngsi
#     #leiofeiAPi
#     # 增加比价操作11
#     # 往场次哦那个
#     # 纵有疾风起。人生不言弃


def test():
    """ jianopan s
    """
    a = "dad j  ffs a "
    b = max(3, 8)
    return b