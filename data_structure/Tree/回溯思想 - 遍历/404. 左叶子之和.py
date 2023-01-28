"""
题目：
    给定二叉树的根节点 root ，返回所有左叶子之和。
"""


class Solution:
    def __init__(self):
        self.res = 0

    def sumOfLeftLeaves(self, root) -> int:
        self.traverse(root)
        return self.res

    def traverse(self, node):
        if node is None:
            return
        if node.left is not None and node.left.left is None and node.left.right is None:
            self.res += node.left.val
        self.traverse(node.left)
        self.traverse(node.right)