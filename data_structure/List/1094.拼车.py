"""
题目：
    车上初始有 capacity 个空座位，车只能向一个方向行驶（也就是说不允许掉头或者改变方向）
    给定整数capacity 和一个数组trips， trip[i] = [numPassengersi, fromi, toi]
    表示第i次旅行有numPassengersi乘客，接他们和放他们呢的位置分别是fromi和toi，这些位置是从汽车的初始位置向东的公里数
    当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false
    1 <= trips.length <= 1000
"""

from diff_array import Difference


def carPooling(trips, capacity):
    """
    :param trips: 某一趟旅行的乘客数
    :param capacity: 车当前的座位数
    :return: False  / True
    """
    df = Difference([0 for _ in range(1001)])
    for t in trips:
        # 当前这站的乘客数
        val = t[0]
        # 第 trip[1] 站乘客上车
        start = t[1]
        # 第 trip[2] 站乘客已经下车，
        # 即乘客在车上的区间是 [trip[1], trip[2] - 1]
        end = t[2] - 1
        df.increment(start, end, val)

    for num in df.result():
        # 客车自始至终不能超载
        if num > capacity:
            return False

    return True
