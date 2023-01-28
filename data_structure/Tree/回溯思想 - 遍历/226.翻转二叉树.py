"""
题目：
    给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
"""


class Solution:
    def invertTree(self, root):
        self.traverse(root)
        return root

    def traverse(self, node):
        if node is None:
            return None
        node.left, node.right = node.right, node.left
        self.traverse(node.left)
        self.traverse(node.right)