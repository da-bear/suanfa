"""
top k 问题
    现在有n个数，设计算法得到前k大的数
    解决思路：
        排序后切片     O(nlogn)
        排序lowb三人组  排前k趟  O(kn)
        堆排序思路   O(nlogk)
"""
import random


def sift_s(li, low, high):
    """
    小根堆
    堆的向下调整（根结点的左右子数都是堆， 但是根结点不满足堆的性质， 向下题哦正使其变成一个堆）
    :param li: 列表
    :param low: 堆的根节点位置index
    :param high: 堆的最后一个位置的index
    :return:
    """
    i = low
    j = 2 * i + 1  # i位置的左孩子
    tmp = li[low]  # 把堆顶存起来
    while j <= high:  # 只要j 位置有数
        if j + 1 <= high and li[j + 1] < li[j]:  # 如果右孩子有并且比较小
            j = j + 1  # j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]  # 将j的值放到i
            i = j  # 这样才能使i往下一层
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


def top_k(li, k):
    """
    :return:
    """
    # 选列表前5个数建立一个小根堆
    heap = li[0:k]
    for i in range((k - 2) // 2, -1, -1):
        sift_s(heap, 0, k - 1)
    # 小根堆建立完成
    for i in range(k, len(l1) - 1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift_s(heap, 0, k - 1)

    # 遍历
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift_s(heap, 0, i-1)

    return heap


if __name__ == '__main__':
    l1 = list(range(100))
    random.shuffle(l1)
    print(top_k(l1, 10))
