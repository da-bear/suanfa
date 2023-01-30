"""
    给定一个N叉树，返回其节点值的层序遍历（从左到右，逐层遍历）

    class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


def levelOrder(root):
    res = []
    if root is None:
        return res
    q = deque()
    # 跟节点入队列
    q.append(root)
    while len(q) > 0:
        # 这一层的节点
        tmp = []
        for _ in range(len(q)):
            node = q.popleft()
            tmp.append(node.val)
            for child in node.children:
                if child is not None:
                    q.append(child)
        res.append(tmp)
    return res

