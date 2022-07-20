# 2022-07-20
"""
题目:
    将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
分析:
    # 代码中还用到一个链表的算法题中是很常见的「虚拟头结点」技巧，也就是 dummy 节点。
    # 你可以试试，如果不使用 dummy 虚拟节点，代码会复杂很多，而有了 dummy 节点这个占位符，可以避免处理空指针的情况，降低代码的复杂性。

    1.如何在 O(n)的时间代价以及 O(1)O(1) 的空间代价完成合并？
        这个问题在面试中常常出现，为了达到空间代价是 O(1)， => 原地调整链表元素的next 指针完成合并

"""
# 导入
from Linked_list.link_list_basic.LList import ListNode, LList, print_node


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


if __name__ == '__main__':
    l1_list = LList()
    l1_data = [1, 2, 4]

    l2_list = LList()
    l2_data = [1, 3, 4]
    for e in l1_data:
        l1_list.append(e)
    for s in l2_data:
        l2_list.append(s)

    print_node(l1_list.head)
    print_node(l2_list.head)

    res = Solution.mergeTwoLists(l1_list.head, l2_list.head)
    print_node(res)
