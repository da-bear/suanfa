"""
题目：
    给定一个单链表 L 的头节点 head ，单链表 L 表示为
        L0 → L1 → … → Ln - 1 → Ln
    将其重新排列后变为
        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2

    不能只是单纯改变节点内部的值，而是需要实际的进行节点交换

    输入：head = [1,2,3,4]
    输出：[1,4,2,3]

分析：
    难点：一个单链表只能从头部向尾部遍历节点，无法从尾部开始向头部遍历节点
    我们可以利用 栈的结构特点，按从头到位的顺序让链表节点入站，那么出栈的顺序就是反过来的

    [1,2 ,3 ,4 ,5 ,6]   偶数
    1 2 3 4 5 6
    1 6 2 5 3 4
            p
            node 4
            nxt = p.next  4   node == nxt node.next = None  break


    [1,2 ,3 ,4 ,5 ,6, 7]  奇数
    1 2 3 4 5 6 7
    1 7 2 6 3 5 4
                p
                node 4
                nxt = p.next  5   node.next = 5  break
"""


def reorderList(head):
    # 创建一个list存放节点
    stk = []
    # 头节点指针
    p = head

    while p is not None:
        stk.append(p)
        p = p.next
    # 将p重新指向
    p = head
    while p is not None:
        # 链表尾部节点
        node = stk.pop()
        nxt = p.next
        if node == nxt or node.next == nxt:
            # 结束条件，链表节点数为奇数或偶数时均适用
            node.next = None
            break
        p.next = node
        node.next = nxt
        p = nxt










