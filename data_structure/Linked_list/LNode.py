"""
单 / 双链表的节点
"""


class LNode(object):
    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


class DLNode(object):
    def __init__(self, val, next_=None, prev=None):
        self.val = val
        self.next = next_
        self.prev = prev
