"""
树是一种数据结构  eg（目录结构）
树是一种可以递归定义的数据结构
树是由n个节点组成的集合
    如果n = 0, 空树
    如果 n > 0， 那么存在1个节点作为树的根结点，其他节点可以分为m个集合， 每个集合本身就是一棵树

一些概念：
    根节点 ， 叶子节点（没有子节点）
    树的深度（高度）
    树的度： 最大的分叉数
    孩子节点 / 父节点
    字树

二叉树：度不超过2的树
    满二叉树：一个二叉树，如果每一层的结点数都达到最大值，则这个二叉树是就是满二叉树
    完全二叉树： 叶节点只能出现在最下层和次下层，并且最下面一层的节点都集中在该层最左边的若干位置二叉树

二叉树的存储方式
    链式存储
    数序存储
    eg: [9, 8, 6, 5, 0, 1, 2, 4, 3]
        父节点和左孩子节点的编号下标关系
            i (c) -> 2i(f) + 1
        父节点和右孩子节点的编号下标关系
            i (c) -> 2i(f) + 2

什么是堆
    大根堆： 一棵完全二叉树，满足任一节点都比其孩子节点大
    小根堆： 一棵完全二叉树，满足任一节点都比其孩子节点小

    堆的向下调整
        假设根结点的左右子树都是堆，但其根节点不满足堆的性质
        可以通过一下向下调整将其变成一个堆

堆排序
    1.建立堆
    2.得到堆顶元素

时间复杂度o（nlogn）
"""

import random
import heapq


def sift(li, low, high):
    """
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
        if j + 1 <= high and li[j + 1] > li[j]:  # 如果右孩子有并且比较大
            j = j + 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]  # 将j的值放到i
            i = j  # 这样才能使i往下一层
            j = 2 * i + 1
        else:
            break
    li[i] = tmp


def heap_sort(li):
    n = len(li)
    # 构造堆
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
    # 建堆完成
    # 挨个出数
    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i -> high 指向当前堆的最后一个元素


if __name__ == '__main__':
    l1 = list(range(100))
    random.shuffle(l1)
    # print(l1)
    # heap_sort(l1)
    # print(l1)

    # 使用python内置的模块来实现堆排序
    heapq.heapify(l1)  # 建堆
    for i in range(len(l1)):
        print(heapq.heappop(l1), end=",")
