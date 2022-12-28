"""
题目：
    给定一个已排序的链表的头head,删除所有重复的元素,使每个元素只出现一次。返回已排序的链表
分析：
    其实和数组去重是一模一样的，唯一的区别是把数组赋值操作变成操作指针而已，你对照着之前的代码来看：

"""


def deleteDuplicates(head):
    if head is None:
        return None
    slow = head
    fast = head

    while fast is not None:
        if slow.val != fast.val:
            slow.next = fast
            slow = slow.next
        fast = fast.next

    # 断开与后面重复元素的链接
    slow.next = None

    return head

