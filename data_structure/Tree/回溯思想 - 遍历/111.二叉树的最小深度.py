"""
    给定一个二叉树，找出其最小深度。
    最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
    说明：叶子节点是指没有子节点的节点。
"""


class Solution:
    def __init__(self):
        self.depth = 0
        self.res = 10 ** 5

    def minDepth(self, root):
        self.traverse(root)
        return self.res if self.res != 10**5 else 0

    def traverse(self, node):
        if node is None:
            return
        self.depth += 1
        if node.left is None and node.right is None:
            self.res = min(self.res, self.depth)
        self.traverse(node.left)
        self.traverse(node.right)
        self.depth -= 1