"""
实现一个hash表
"""


class LinkList:
    """
    实现一个单链表的类
    """

    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node is not None:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.val
            else:
                return StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, val):
        p = LinkList.Node(val)
        if self.head is None:
            self.head = p
            self.tail = p
        else:
            self.head.next = p
            self.tail = p

    def extend(self, iterable):
        for val in iterable:
            self.append(val)

    def find_val(self, val):
        p = self.head
        while p is not None:
            if p.val == val:
                return p
            p = p.next
        return None

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<+" + ",".join(map(str, self)) + ">>"


class HashTable:
    """
    hash table
    """
    def __init__(self, size = 100):
        self.size = size



if __name__ == '__main__':
    lk = LinkList([1, 2, 3, 4, 5])
    for i in lk:
        print(i)
