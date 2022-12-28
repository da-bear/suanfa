"""
题目：
    给你两个单链表的头节点 headA 和 headB, 请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回null。
    题目数据保证整个链式结构中不存在环。

分析：
    如果不用额外的空间，只使用两个指针，你如何做呢？
    难点在于，由于两条链表的长度可能不同，两条链表之间的节点无法对应
    如果用两个指针 p1 和 p2 分别在两条链表上前进，并不能同时走到公共节点，也就无法得到相交节点 c1
    # todo 解决这个问题的关键是，通过某些方式，让 p1 和 p2 能够同时到达相交节点 c1。
    所以，我们可以让p1遍历完链表A之后开始遍历链表B，让p2遍历完链表B之后开始遍历链表A，这样相当于「逻辑上」两条链表接在了一起。
    如果这样进行拼接，就可以让 p1 和 p2 同时进入公共部分，也就是同时到达相交节点 c1：

    那你可能会问，如果说两个链表没有相交点，是否能够正确的返回 null 呢？
    这个逻辑可以覆盖这种情况的，相当于 c1 节点是 null 空指针嘛，可以正确返回 null。
"""


def getIntersectionNode(headA, headB):
    """
    :param headA: 链表A
    :param headB: 链表B
    :return:node
    """
    p1 = headA
    p2 = headB

    while p1 != p2:
        if p1 is None:
            p1 = headB  # 如果headA遍历完就让p1去遍历headB
        else:
            p1 = p1.next

        if p2 is None:
            p2 = headA
        else:
            p2 = p2.next

    return p1












