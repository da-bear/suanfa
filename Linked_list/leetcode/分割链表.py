# 2022-07-19
"""
# 给你一个链表的头节点 head 和一个特定值x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你应当 保留 两个分区中每个节点的初始相对位置

"""
# 导入
from Linked_list.link_list_basic.LList import ListNode, LList, print_node


class Solution:

    @staticmethod
    def partition(head: ListNode, x: int) -> ListNode:
        # 存小于x的链表
        s_node = ListNode(-1)
        # 存大于x的链表
        l_node = ListNode(-1)
        # s_node 指针
        s_p = s_node
        # l_node 指针
        l_p = l_node

        # head 指针
        h_p = head

        while h_p:
            if h_p.val < x:
                s_p.next = h_p
                s_p = s_p.next
            else:
                l_p.next = h_p
                l_p = l_p.next
            # 切断原链表中每个节点的的引用,如果此处不做修改，那么在循环结束后需要处理l_p.next指针
            tmp = h_p.next
            h_p.next = None
            h_p = tmp
            # h_p = h_p.next

        # while循环结束后,需要将l_p.next的指针置空，因为当前节点复用的是原链表的节点，其next的指针可能指向一个小于x的节点
        # 需要切断这个引用, 并将s_p.next 指针指向l_node.next 实现链表的拼接
        # s_node 的next指针即为答案

        # l_p.next = None
        # 连接两个链表
        s_p.next = l_node.next
        return s_node.next


if __name__ == '__main__':
    # 构造一个链表  l_list
    l_list = LList()
    test_data = [1, 4, 3, 2, 5, 2]
    for e in test_data:
        l_list.append(e)
    # 控制台打印node的元素
    print("params_l_list")
    print_node(l_list.head)
    print("**" * 50)
    print("target_l_list")
    res = Solution.partition(l_list.head, 3)
    print_node(res)
