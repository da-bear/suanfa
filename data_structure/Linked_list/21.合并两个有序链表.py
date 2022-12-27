"""
题目:
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
分析:
    # 代码中还用到一个链表的算法题中是很常见的「虚拟头结点」技巧，也就是 dummy 节点。
    # 你可以试试，如果不使用 dummy 虚拟节点，代码会复杂很多，而有了 dummy 节点这个占位符，可以避免处理空指针的情况，降低代码的复杂性。

    1.如何在 O(n)的时间代价以及 O(1)O(1) 的空间代价完成合并？
        这个问题在面试中常常出现，为了达到空间代价是 O(1)， => 原地调整链表元素的next 指针完成合并

"""

from LNode import LNode


def mergeTwoLists(list1, list2):
    """
    双指针合并两个双序链表
    """
    # 创建虚拟头节点
    dummy = LNode(-1)
    p = dummy
    # 链表的指针
    p1 = list1
    p2 = list2

    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.nex
        p = p.next

    p.next = p1 if p1 is not None else p2
    # dummy 始终代表的的是新链表的头节点 p代表新链表的指针
    return dummy.next







