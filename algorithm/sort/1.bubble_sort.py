"""
2022-11-12
冒泡排序：
    列表每两个相邻的数，如果前面比后面大，则交换这两个数
    一趟排序完成后，有序区添加一个数，无序区增加一个数
    代码关键： 趟、无序区、有序区
"""
import random


def bubble_sort(li):
    """
    时间复杂度O(n2)
    """
    for i in range(len(li) - 1):  # i 表示冒泡的趟
        exchange = False
        for j in range(len(li) - i - 1):  # 无序区
            # if l1[j] > l1[j + 1]: # 升序
            if li[j] > li[j + 1]:  # 降序
                li[j + 1], li[j] = li[j], li[j + 1]
                exchange = True
        # print(li)
        if not exchange:
            break


if __name__ == '__main__':
    l1 = [random.randint(0, 10000) for i in range(10000)]
    l2 = [1, 2, 3, 5, 6, 7, 8, 9]
    print("before bubble sort:", l1)
    bubble_sort(l1)
    print("after bubble sort:", l1)
    bubble_sort(l2)
    print(l2)
