# 2022-07-20
"""
题目:
    给你一个链表数组，每个链表都已经按升序排列
    请你将所有链表合并到一个升序链表中，返回合并后的链表。

分析:


"""
# 导入
from Linked_list.link_list_basic.LList import ListNode, LList, print_node


class Solution:

    @staticmethod
    def mergeKLists_1(lists):
        # 虚拟头节点
        t_list = ListNode(-1)
        # 指针
        t_p = t_list
        node_val_list = []
        for l_list in lists:
            while l_list is not None:
                node_val_list.append(l_list.val)
                l_list = l_list.next

        tmp = sorted(node_val_list)
        for node_val in tmp:
            if t_p:
                while t_p.next is not None:
                    t_p = t_p.next
                t_p.next = ListNode(node_val)

        return t_list.next

    @staticmethod
    def mergeKLists_2(lists):
        # 虚拟头节点
        t_list = ListNode(-1)
        # 指针
        t_p = t_list
        return None


def solution_test():
    l1 = LList()
    l1_d = [1, 4, 5]
    l2 = LList()
    l2_d = [1, 3, 4]
    l3 = LList()
    l3_d = [2, 6]

    for e in l1_d:
        l1.append(e)
    for s in l2_d:
        l2.append(s)
    for m in l3_d:
        l3.append(m)

    return [l1.head, l2.head, l3.head]


def heapq_test():
    import heapq
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    heap = []
    # heappush(heap, num)，先创建一个空堆，然后将数据一个一个地添加到堆中。每添加一个数据后，heap都满足小顶堆的特性
    for num in array:
        heapq.heappush(heap, num)
    print("array:", array)
    print("heap: ", heap)
    # heapify(array)，直接将数据列表调整成一个小顶堆(调整的原理参考上面堆排序的文章，heapq库已经实现了)。
    heapq.heapify(array)
    print("array:", array)


if __name__ == '__main__':
    # s_list = solution_test()
    # res = Solution.mergeKLists_1(s_list)
    # print_node(res)
    heapq_test()
