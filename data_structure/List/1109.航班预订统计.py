"""
题目：
    这里有n个航班， 他们分别从 1-n 进行编号
    我们这二有一份航班预定表，表中第i条预定记录bookings[i] = [i , j , k],
    意味着从i到j的每个航班预定了k个座位
    请你返回一个长度为n的数组answer，按航班编号顺序返回每个航班上预定的座位数
"""
from diff_array import Difference


def corpFlightBookings(bookings, n):
    """
    使用差分数组的思想
    """
    # 构造一个长度为n的数组
    df = Difference([0 for _ in range(n)])
    for b in bookings:
        df.increment(b[0] - 1, b[1] - 1, b[2])
    return df.result()


