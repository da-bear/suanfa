"""
题目：
    给你单链表的头节点head，请你反转链表，并返回反转后的链表。
分析：
    递归的方式
    递归函数的定义
"""


# 递归函数的定义输入一个节点 head，将「以 head 为起点」的链表反转，并返回反转之后的头结点。
def reverseList(head):
    # 如果是空节点或者是只有一个节点，那么返回head
    if head is None or head.next is None:
        return head
    # 将head之后的节点反转，并返回反转后的头节点
    last = reverseList(head.next)
    # head.next 是反转后的末尾节点， 将head.next.next 反向指回head
    head.next.next = head
    # 此时head作为反转链表的尾节点，将head.next 置位None
    head.next = None
    return last
