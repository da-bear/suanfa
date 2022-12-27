"""
题目：
    给定一个链表，返回链表开始入环的第一个节点，从链表的头节点开始沿着next指针进入环的第一个节点为环的入口节点，如果链表无环，则返回 null。
    为了表示给定链表中的环，我们使用整数pos来表示链表尾连接到链表中的位置（索引从0开始。如果pos是-1，则在该链表中没有环，
    注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

分析：
    如何判断链表是否有环
        判断链表是否包含环属于经典问题了，解决方案也是用快慢指针：
        每当慢指针 slow 前进一步，快指针 fast 就前进两步。
        如果 fast 最终遇到空指针，说明链表中没有环；如果fast最终和slow相遇，那肯定是 fast超过了slow一圈，说明链表中含有环。


    如何寻找环的起点
    当快慢指针相遇时，让其中任一个指针指向头节点，然后让它俩以相同速度前进，再次相遇时所在的节点位置就是环开始的位置。
        1 - 我们假设快慢指针相遇时，慢指针 slow 走了 k 步，那么快指针 fast 一定走了 2k 步
        2 - fast 一定比 slow 多走了 k 步，这多走的 k步 其实就是 fast 指针在环里转圈圈，所以 k 的值就是环长度的「整数倍」
        3 - 假设相遇点距环的起点的距离为m，环的起点距头结点 head 的距离为 k-m，也就是说如果从 head 前进 k-m步 就能到达环起点
        4 - 如果从相遇点继续前进k-m步，也恰好到达环起点。因为从相遇点开始走k 步 可以转回到相遇点，那走 k-m步 肯定就走到环起点了
        5 - 只要我们把快慢指针中的任一个重新指向 head，然后两个指针同速前进，k-m步 后一定会相遇，相遇之处就是环的起点了。
"""


def hasCycle(head):
    """
    判断是否有环
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


def detectCycle(head):
    """
    给定一个链表，返回链表开始入环的第一个节点
    """
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # 相遇表示有环
            break
    else:
        return None  # 没有环
    # 此时要计算环的起点

    # 将满指针指向head, 快慢指针同步向前，下一次相遇就是环的起点
    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next

    return slow
