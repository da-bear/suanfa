class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LinkedListUnderflow(ValueError):
    pass


class LCList(object):
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p  # 建立一个节点的环
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next   # 更新尾部作用域

    def pop_pre(self):  # 前端弹出
        if self._rear is None:
            raise LinkedListUnderflow("in pop of LCList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next




l_list = LCList()
# l_list.prepend(1)
# l_list.prepend(2)
# l_list.prepend(3)
# l_list.prepend(4)


l_list.append(1)
l_list.append(2)
l_list.append(3)
l_list.append(4)

# l_list.pop_tail()
l_list.printall()

