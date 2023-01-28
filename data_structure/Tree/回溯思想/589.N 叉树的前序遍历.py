"""
题目：
    给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历
"""


class Solution:
    def __init__(self):
        self.res = []

    def preorder(self, root):
        self.traverse(root)
        return self.res

    def traverse(self, node):
        if node is None:
            return
        self.res.append(node.val)
        for c in node.children:
            self.traverse(c)