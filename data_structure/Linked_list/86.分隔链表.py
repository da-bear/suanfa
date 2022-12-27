"""
题目：
    给你一个链表的头节点 head 和一个特定值 x，请你对链表进行分隔，
        使得所有小于x的节点都出现在大于或等于x的节点之前。
        你应当保留两个分区中每个节点的初始相对位置
"""
from LNode import LNode


def partition(head, x):
    """
    :param head: 链表头节点
    :param x: 分隔的值x
    :return: 分隔后再拼接的链表
    """
    # 虚拟头节点，存放链表中小于x的node
    dummy1 = LNode(-1)
    # 虚拟头节点，存放链表中大于等于x的node
    dummy2 = LNode(-1)
    p1 = dummy1
    p2 = dummy2
    p = head
    while p is not None:
        if p.val < x:
            p1.next = p
            p1 = p1.next
        else:
            p2.next = p
            p2 = p2.next

        # 断开原链表中的每个节点的next指针
        tmp = p.next
        p.next = None
        p = tmp
    # 将分隔的两段链表拼接
    p1.next = dummy2.next

    return dummy1.next










