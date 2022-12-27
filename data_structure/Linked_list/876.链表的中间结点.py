"""
题目：
    给定一个头结点为 head 的非空单链表，返回链表的中间结点，如果有两个中间结点，则返回第二个中间结点

分析：
    问题的关键也在于我们无法直接得到单链表的长度n，常规方法也是先遍历链表计算n，再遍历一次得到第n/2个节点，也就是中间节点。
    如果想一次遍历就得到中间节点，也需要耍点小聪明，使用「快慢指针」的技巧：
    我们让两个指针 slow 和 fast 分别指向链表头结点 head
    TODO：每当慢指针 slow 前进一步，快指针 fast 就前进两步，这样，当 fast 走到链表末尾时，slow 就指向了链表中点。
"""


def middleNode(head):
    """
    :param head: 链表
    :return: 链表的中间节点
    """
    slow = head
    fast = head
    # 1 3 5 7
    # 1 2 3 4
    while fast is not None and fast.next is not None: # fast.next is not None 来控制如果有两个中间节点， 返回第二个
        fast = fast.next.next
        slow = slow.next

    return slow














