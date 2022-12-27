"""
题目：
    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
分析：
    要删除倒数第n个节点，就得获得倒数第 n + 1 个节点的引用，可以用我们实现的 findFromEnd 来操作
注意：
    使用了虚拟头结点的技巧，也是为了防止出现空指针的情况，
    比如说链表总共有 5 个节点，题目就让你删除倒数第 5 个节点，也就是第一个节点，那按照算法逻辑，应该首先找到倒数第 6 个节点。
    但第一个节点前面已经没有节点了，这就会出错。但有了我们虚拟节点 dummy 的存在，就避免了这个问题，能够对这种情况进行正确的删除

"""
from LNode import LNode


def findKthFromEnd(head, k):
    p1 = head  # 指针p1
    # p1 向后走k步
    for _ in range(k):
        p1 = p1.next
    p2 = head  # 指针p2
    # p1 和 p2 同时向后走
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2


def removeNthFromEnd(head, n):
    """
    :param head: 链表头节点
    :param n: 删除的元素n
    :return: 删除元素后的链表
    """
    dummy = LNode(-1)
    dummy.next = head
    x = findKthFromEnd(dummy, n+1)
    x.next = x.next.next
    return dummy.next




