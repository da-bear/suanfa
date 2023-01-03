"""
题目：
    给你链表的头节点 head ，每k个节点一组进行翻转，请你返回修改后的链表。
    k是一个正整数，它的值小于或等于链表的长度。如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。
    你不能只是单纯改变节点内部的值，而是需要实际进行节点交换。

分析：
    1-  使用迭代方法来反转链表
    2 - 反转以 a 为头结点的链表」其实就是「反转 a 到 null 之间的结点」，那么如果让你「反转 a 到 b 之间的结点
        只要更改函数签名，并把上面的代码中 null 改成 b 即可

    3 -

"""


def reserve_1(head):
    """
    使用迭代方式反转链表
    """
    pre = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    return pre


def reserve(node_a, node_b):
    """
    「反转 a 到 b 之间的结点」
    """
    pre = None
    cur = node_a
    while cur != node_b:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt

    return pre


def reverseKGroup(head, k):
    """
    k 个一组反转链表
    """
    if head is None:
        return
    a, b = head, head
    for _ in range(k):
        if b is None:
            return head
        b = b.next

    # 反转 [a, b]
    new_head = reserve(a, b)
    a.next = reverseKGroup(b, k)
    return new_head



