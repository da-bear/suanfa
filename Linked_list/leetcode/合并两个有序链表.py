class ListNode(object):
    def __init__(self, elem, next_=None):
        self.val = elem
        self.next = next_


class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        # 虚拟头节点
        pre_head = ListNode(-1)

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
