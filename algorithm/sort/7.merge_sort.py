"""
归并排序
    时间复杂度O(nlogn)
    sort
    递归有空间复杂度 o(logn) 层
"""
import random


def test_merge(a, b):
    i, j = 0, 0  # a,b 两个list的指针
    tmp = []
    while i <= len(a) - 1 and j <= len(b) - 1:
        # 双指针
        if a[i] < b[j]:
            tmp.append(a[i])
            i += 1
        elif a[i] == b[j]:
            tmp.append(a[i])
            i += 1
            j += 1
        else:
            tmp.append(b[j])
            j += 1

    # 因为 i 或者j + 1 后跳出循环，但是值没有添加到tmp中
    if i < len(a) - 1:
        tmp += a[i:]
    if j < len(b) - 1:
        tmp += b[i:]

    return tmp


def merge(li, low, mid, high):
    """
    :param li: 列表
    :param low: 第一段的起点
    :param mid: 分界点
    :param high: 第二段的起点
    :return:
    """
    # 指针
    i = low
    j = mid + 1
    tmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1

    while i <= mid:
        tmp.append(li[i])
        i += 1
    while j <= high:
        tmp.append(li[j])
        j += 1

    li[low: high + 1] = tmp


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)


if __name__ == '__main__':
    # a1 = [2, 3, 4, 5]
    # b1 = [1, 2, 3, 4, 7, 8, 9]
    #
    # print(test_merge(a1, b1))

    l1 = list(range(100))
    random.shuffle(l1)
    print(l1)
    merge_sort(l1, 0, len(l1) - 1)
    print(l1)
