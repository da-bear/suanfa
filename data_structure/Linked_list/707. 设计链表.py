"""
设计链表的实现。
    可以选择使用单链表或双链表。
        单链表中的节点应该具有两个属性-> val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。
    如果使用双向链表，
         还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：
    get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
    addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
    addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
    addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，
                        则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
    deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点
"""

from data_structure.Linked_list.LNode import LNode, DLNode


class LList:
    def __init__(self):
        self.head = None
        self.size = self._size()

    def _size(self):
        p, n = self.head, 0
        while p is not None:
            n += 1
            p = p.next
        return n

    def get(self, index):
        """
        查询index -> val
        """
        if index < 0 or index >= self.size:
            return -1
        p = self.head
        for _ in range(index + 1):
            p = p.next
        return p.val

    def addAtHead(self, val):
        """
        头插法
        """
        self.addAtIndex(0, val)

    def addATail(self, val):
        """
        尾插法
        """
        self.addAtIndex(self.size - 1, val)

    def addAtIndex(self, index, val):
        """
        链表插入
        """
        if index < 0 or index >= self.size:
            return

        self.size += 1
        prev = self.head
        if index > 0:
            for _ in range(index):
                prev = prev.next
        p = LNode(val)
        p.next = prev.next
        prev.next = p


    def delete_at_index(self, index, val):
        """
        删除节点
        """
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
