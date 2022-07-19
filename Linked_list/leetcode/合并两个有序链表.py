class ListNode(object):
    def __init__(self, elem, next_=None):
        self.val = elem
        self.next = next_


# 代码中还用到一个链表的算法题中是很常见的「虚拟头结点」技巧，也就是 dummy 节点。
# 你可以试试，如果不使用 dummy 虚拟节点，代码会复杂很多，而有了 dummy 节点这个占位符，可以避免处理空指针的情况，降低代码的复杂性。
class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        # 虚拟头节点
        pre_head = ListNode(-1)
        # prev 可以理解为指针
        prev = pre_head
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 if l1 is not None else l2

        return pre_head.next
