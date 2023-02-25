
class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class Demo(object):
    # 打印链表
    def printList(self, head):
        if head is None:
            return
        print(head.value)
        self.printList(head.next)

    # 1 - 2  - None
    def addLast(self, head, val):
        """
        递归的修改数据结构
        """
        if head is None:
            return ListNode(val)

        head.next = self.addLast(head.next, val)
        return head

    # 1 - 2  - None
    def removeLast(self, head):
        if head.next is None:
            return None
        head.next = self.removeLast(head.next)
        return head

