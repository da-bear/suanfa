"""
    队列和栈是操作受限的数据结构
    底层用linkList 也可以用arrayList
"""

from data_structure.Linked_list.MyLList import MyLinkedList1


class MyLinkedStack:

    def __init__(self):
        self.list = MyLinkedList1()

    def push(self, e):
        self.list.addLast(e)

    def pop(self):
        return self.list.removeLast()

    def peek(self):
        return self.list.getLast()


class MyLinkedStack2:
    def __init__(self):
        self.stack = []

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
