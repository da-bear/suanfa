"""
快速排序：
    找到一个数将其归位，使得这个数左侧都是比它小的数，右侧都是比它大的数： -> 操作1
    将操作1中归位的数的两侧同时进行操作1
    递归操作完成排序

时间复杂度 O（nlogn）
问题：
    递归：会消耗一定的系统资源
"""
from algorithm.cal_time import timeit
import random
import sys

sys.setrecursionlimit(1000)  # 修改递归最大深度


def partition(li, left, right):
    """
    将li[left: right] li[left]值进行归位
    """
    tmp = li[left]  # 将要归位的数存起来， left存在一个空位
    while left < right:
        while left < right and li[right] >= tmp:  # 从右往左寻找比tmp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # right: 从右往左找到一个比tmp小的数，将右边的值写到左边的空位上

        while left < right and li[left] <= tmp:  # 从左往右寻找比tmp小大的数
            left += 1  # 往右一步
        li[right] = li[left]  # 将找到的值写到右边的空位上

    li[left] = tmp  # left 指针存tmp, 将tmp归位
    return left


def _quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        _quick_sort(li, left, mid - 1)
        _quick_sort(li, mid + 1, right)


@timeit
def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


if __name__ == '__main__':
    l1 = list(range(10000))
    random.shuffle(l1)
    quick_sort(l1)
