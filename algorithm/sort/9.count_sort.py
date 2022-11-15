"""
    计数排序
        对列表进行排序，已知列表中的数的范围都在 0 -100 之间
        设计时间复杂度O(n) 的算法
        之前的排序 -> 比较排序最快也是nlogn
"""

import random


def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count + 1)]  # 最大的数  + 1
    for val in li:
        count[val] += 1
    li.clear()
    for ind, v in enumerate(count):
        for i in range(v):
            li.append(ind)


if __name__ == '__main__':
    l1 = [random.randint(0, 100) for _ in range(150)]
    random.shuffle(l1)
    print(l1)
    count_sort(l1)
    print(l1)
