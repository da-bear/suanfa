"""
题目:
    给你一个链表数组，每个链表都已经按升序排列
    请你将所有链表合并到一个升序链表中，返回合并后的链表。

分析:
    合并 k 个有序链表的逻辑类似合并两个有序链表，难点在于，如何快速得到 k 个节点中的最小节点，接到结果链表上？
    这里我们就要用到 优先级队列（二叉堆） 这种数据结构，把链表节点放入一个最小堆，就可以每次获得 k 个节点中的最小节点：

"""
import heapq
from LNode import LNode


def heapq_test():
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

    # heappop(heap)，将堆顶的数据出堆，并将堆中剩余的数据构造成新的小顶堆
    heap_sort = [heapq.heappop(heap) for _ in range(len(heap))]
    print("heap sort result: ", heap_sort)


def mergeKLists(lists):
    """
    分析: 可以将k个链表中
    :param lists:  List[Optional[ListNode]]
    :return: Optional[ListNode]
    """
    tmp = []
    dummy = LNode(-1)  # 虚拟头节点
    p = dummy
    for node in lists:
        while node is not None:
            tmp.append(node.val)
            node = node.next

    tmp.sort()
    for val in tmp:
        p.next = LNode(val)
        p = p.next

    return dummy.next


def mergeKLists_2(lists):
    """
    使用最小堆的特性
    """
    dummy = LNode(-1)
    p = dummy
    # 创建堆
    heap = []
    for node in lists:
        while node is not None:
            heapq.heappush(heap, node.val)
            node = node.next

    while heap and p:
        p.next = LNode(heapq.heappop(heap))
        p = p.next

    return dummy.next



