"""
题目：
    给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
    请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表

分析：
    什么叫反转单链表的一部分呢，就是给你一个索引区间，让你把单链表中这部分元素反转，其他部分不变

    注意这里的索引是从 1 开始的。迭代的思路大概是：
        先用一个for循环找到第m个位置，然后再用一个for循环将m和n之间的元素反转。
        但是我们的递归解法不用一个 for 循环，纯递归实现反转。

    一 ：反转整个链表
    二 ：反转链表前 N 个节点

        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        反转前3个节点

        1 <- 2 <- 3   4 -> 5 -> 6 -> 7
        |_____________^

    三 ：反转某一部分节点 [m, n]
        如果 m == 1 那么就是上述情形
        如果 m != n
            那么如果我们把head的索引视为1，那么我们是想从第m个元素开始反转
            如果把 head.next的索引视为1呢？那么相对于 head.next，反转的区间应该是从第m-1个元素开始的；
            那么对于 head.next.next..........next
                        < --------- m ---------->

"""
tmp = None


# 反转以head为起点的N个节点，返回新的头节点
def reserveN(head, n):
    global tmp
    if n == 1:
        # 当递归到此处时候，此时head代表最后一个node，node.next 就是初始链表的第n+1个节点
        tmp = head.next
        return head

    # 以head.next为起点，需要反转前n-1个节点
    last = reserveN(head.next, n-1)

    head.next.next = head
    # 让反转之后的 head 节点和后面的节点连起来
    head.next = tmp

    return last


def reverseBetween(head, left, right):
    """
    :param head: 链表头节点
    :param left: 反转部分的起点
    :param right: 反转部分的终点
    :return: 反转后的链表
    """
    # base case
    if left == 1:
        return reserveN(head, right)

    # 前进到反转的起点触发 base case
    head.next = reverseBetween(head.next, left - 1, right - 1)
    return head

