"""
动手实现单链表类
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


# 单链表实现
class MyLinkedList1:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    # --------- 增 -----------
    def addFirst(self, e):
        """
        头插法
        """
        x = ListNode(e)
        x.next = self.head.next
        self.head.next = x
        self.size += 1

    def addLast(self, e):
        """
        尾插法
        """
        x = ListNode(e)
        if self.size >= 1:
            tail = self.getNode(self.size - 1)
        else:
            tail = self.head

        tail.next = x

        self.size += 1

    def add(self, index, element):
        """
        添加元素到index位置
        """
        self.checkPositionIndex(index)
        if index == self.size:
            self.addLast(index)
            return

        # 新加节点
        x = ListNode(element)
        # 获取 index 位置的节点 p
        p = self.getNode(index)
        # 获取 index - 1 位置的节点， 将新的节点x放置在index 之前
        if index - 1 >= 0:
            tmp = self.getNode(index - 1)
        else:
            tmp = self.head

        # tmp - x - p
        tmp.next = x
        x.next = p

        self.size += 1

    # ------------- 删 --------------
    def removeFirst(self):
        if self.isEmpty():
            raise NotImplemented
        x = self.head.next
        self.head.next = self.head.next.next
        x.next = None
        self.size -= 1

        return x.val

    def removeLast(self):
        if self.isEmpty():
            raise NotImplemented
        # last index: self.size - 1
        x = self.getNode(self.size - 1)

        # 获取last节点之前的节点
        if self.size - 2 > 0:
            tmp = self.getNode(self.size - 2)
        else:
            tmp = self.head
        tmp.next = None
        x.next = None

        self.size -= 1
        return x.val

    def remove(self, index):
        self.checkElementIndex(index)
        p = self.getNode(index)
        # p 之前的node
        if index - 1 >= 0:
            prev = self.getNode(index - 1)
        else:
            prev = self.head

        prev.next = p.next
        p.next = None

        self.size -= 1
        return p.val

    # ------------- 查 -------------
    def getFirst(self):
        if self.isEmpty():
            raise IndexError
        return self.head.next.val

    def getLast(self):
        if self.isEmpty():
            raise IndexError

        return self.getNode(self.size - 1).val

    def get(self, index):
        self.checkElementIndex(index)
        p = self.getNode(index)
        return p.val

    def getNode(self, index):
        p = self.head.next
        for _ in range(index):
            p = p.next
        return p

    def isEmpty(self):
        return self.size == 0

    def isElementIndex(self, index):
        return 0 <= index <= self.size

    def isPositionIndex(self, index):
        return 0 <= index < self.size

    # --- 检查index索引位置是否可以存在元素 -------
    def checkElementIndex(self, index):
        if not self.isElementIndex(index):
            raise IndexError

    # ---- 检查index索引位置是否可以添加元素 -------
    def checkPositionIndex(self, index):
        if not self.isPositionIndex(index):
            raise IndexError
