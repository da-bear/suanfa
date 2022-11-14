"""
希尔排序
    希尔排序（shell sort）是一种分组插入排序算法
    首先取一整数d1 = n / 2， 将元素分为d1个组， 每组相邻两个元素之间距离为d1，在各组内进行直接插入排序
    取第二个整数d2 = d1 / 2， 重复上述分组的排序过程，知道di = 1，即所有的元素在同一组内直接插入排序
    希尔排序每趟并不是某些元素有序，而是使整体数据越来越接近有序，最后一趟排序使得所有数据有序
"""
import random


# 插入排序
def insert_sort_gap(li, gap):
    """
    再插入排序的基础上修改
    """
    # 复习一遍插入排序要点（手里的牌，有序区，无序区），最开始手里有一张牌 ->有序区
    # 遍历无序区
    for i in range(gap, len(li) - 1):
        tmp = li[i]  # 摸出的牌
        j = i - gap  # 有序区的最大index
        # 移动有序区的数，将tmp放入合适位置(当值比tmp大的时候需要移动)
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        # 挪动数结束
        li[j + gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


if __name__ == '__main__':
    l1 = list(range(100))
    random.shuffle(l1)
    print(l1)
    shell_sort(l1)
    print(l1)
