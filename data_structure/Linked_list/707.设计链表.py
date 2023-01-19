"""
题目：
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


    0 <= index, val <= 1000
    请不要使用内置的 LinkedList 库。
    get, addAtHead, addAtTail, addAtIndex 和 deleteAtIndex 的操作次数不超过 2000
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


# 但链表
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def getNode(self, index):
        p = self.head
        for _ in range(index + 1):
            p = p.next
        return p

    def get(self, index: int):
        if index < 0 or index >= self.size:
            return -1
        p = self.getNode(index)
        return p.val

    def addAtHead(self, val: int):
        x = ListNode(val)
        x.next = self.head.next
        self.head.next = x
        self.size += 1

    def addAtTail(self, val: int):
        x = ListNode(val)
        if self.size >= 1:
            tail = self.getNode(self.size - 1)
        else:
            tail = self.head
        tail.next = x
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None

        if index == self.size:
            self.addAtTail(val)
            return

        x = ListNode(val)
        p = self.getNode(index)
        if index - 1 >= 0:
            tmp = self.getNode(index - 1)
        else:
            tmp = self.head

        tmp.next = x
        x.next = p
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return None
        # 获取index 处的node
        if index - 1 >= 0:
            tmp = self.getNode(index - 1)
        else:
            tmp = self.head
        tmp.next = tmp.next.next
        self.size -= 1


if __name__ == '__main__':
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    print(obj.get(1))
    obj.deleteAtIndex(1)
    print(obj.get(1))

