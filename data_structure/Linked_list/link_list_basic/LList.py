

def print_node(p):
    while p is not None:
        print(p.val, end=',')
        if p.next is None:
            print('', end='')
        p = p.next
    print('')


class ListNode(object):
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


# 基于节点类ListNode定义一个单链表对象的类
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, val):
        self._head = ListNode(val, self._head)

    def append(self, val):
        if self._head is None:
            self._head = ListNode(val)
            return None
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = ListNode(val)

    def traverse(self):
        p = self._head
        while p:
            yield p.val
            p = p.next

    def find(self, value):
        p = self._head
        while p is not None:
            if value == p.val:
                return p.val
            p = p.next
        else:
            raise LinkedListUnderflow("no item")

    def length(self):
        p, n = self._head, 0
        while p is not None:
            n += 1
            p = p.next
        return n

    def pop_head(self):
        if self._head is None:
            # 无节点引发异常
            raise LinkedListUnderflow("in pop")
        e = self._head.val
        self._head = self._head.next
        return e

    def pop_tail(self):
        if self._head is None:  # 空表
            raise LinkedListUnderflow("in pop last")
        p = self._head
        if p.next is None:  # 表中只有一个元素
            e = p.val
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.val
        p.next = None
        return e

    def print_all(self):
        p = self._head
        while p is not None:
            print(p.val, end='')
            if p.next is None:
                print(',', end='')
            p = p.next
        print('')

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.val):
                yield p.val
            p = p.next

    @property
    def head(self):
        return self._head


# l_list = LList()
# l_list.append(2)
# l_list.append(3)
# l_list.append(4)
# l_list.append(5)

# l_list.pop_tail()
# for val in l_list.traverse():
#     print(val)

# print(l_list.length())
# print(l_list.find(7))
#l_list.printall()
