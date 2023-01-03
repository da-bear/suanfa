"""
题目：
    给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false

分析：
    这道题的关键在于，单链表无法倒着遍历，无法使用双指针技巧。
    最简单的办法就是，把原始链表反转存入一条新的链表，然后比较这两条链表是否相同

    1 - 借助二叉树后序遍历的思路，不需要显式反转原始链表也可以倒序遍历链表
        核心逻辑是什么呢？实际上就是把链表节点放入一个栈，然后再拿出来，这时候元素顺序就是反的
            算法的时间复杂度和空间复杂度都是O(N)

    2 - 优化空间复杂度的解法
        - 先通过快慢指针找到链表的中点
        - 从中点反转后半部分的链表
        - 比较回文串
        算法总体的时间复杂度 O(N)，空间复杂度 O(1)，已经是最优的了。
        我知道肯定有读者会问：这种解法虽然高效，但破坏了输入链表的原始结构，能不能避免这个瑕疵呢？
        其实这个问题很好解决，关键在于得到p, q这两个指针位置



"""
# left = None
#
#
# def isPalindrome_1(head):
#     """
#     判断是否为回文链表
#     """
#     global left
#     left = head
#     return traverse(head)
#
#
# def traverse(right):
#     if right is None:
#         return True
#     global left
#     res = traverse(right.next)
#     res = res and (right.val == left.val)
#     left = left.next
#     return res


def reserve(head):
    """
    将以head为头节点的链表反转
    """
    pre = None
    cur = head
    while cur is not None:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre


def isPalindrome(head):
    # 1. 快慢指针找到链表的中点
    slow = fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    # 如果链表节点个数是奇数，需要slow.next 作为要反转链表head
    if fast is not None:
        slow = slow.next

    left = head
    right = reserve(slow)
    while right is not None:
        if right.val != left.val:
            return False
        left = left.next
        right = right.next

    return True









