"""
题目：
    假设你有一个长度为n的数组，初使情况下所有的数字均为0，你将会被给出k个更新操作，
    其中每个操作会被表示为一个三元组，[startIndex, endIndex, inc], 你需要将子数组A[startIndex....endIndex]
    包括（startIndex 和 endIndex）
    请返回k次操作后的数组

分析：
    TODO：技巧 -> 差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减
    1 - 将nums数组构造一个diff差分数组，diff[i] 就是nums[i] 和 nums[i - 1]之差
        diff = [0 for _ in range(len(nums))]
        diff[0] = nums[0]
        for i in range(1, len(nums)):
            diff [i] = nums[i] - nums[i - 1]

    2 - 通过差分数组可以推出原始数组代码
        res = []
        res[0] = diff[0]
        for i in range(1, len(nums)):
            res[i] = res[i - 1] + diff[i]


    3 - 通过差分数组进行快速的增减操作
        如果想对区间nums[i...j] (包含i and j)  的元素全部加3，那么只需要将diff[i] += 3,然后再让diff[j+1] -=3
"""
from diff_array import Difference


def getModifiedArray(length, updates):
    """
    :param length: 初始化一个长度为5的数组
    :param updates:对指定区间进行对应的操作
    :return: 返回操作后的数组
    """
    df = Difference([0 for _ in range(length)])
    for u in updates:
        df.increment(u[0], u[1], u[2])
    return df.result()



