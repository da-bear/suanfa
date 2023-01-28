"""
题目：
    给定一个 N 叉树，找到其最大深度。
    最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
    N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）
"""


class Solution:
    def __init__(self):
        self.depth = 0
        self.res = 0

    def maxDepth(self, root):
        self.traverse(root)
        return self.res

    def traverse(self, node):
        if node is None:
            return
        self.depth += 1
        self.res = max(self.res, self.depth)
        for c in node.children:
            self.traverse(c)
        self.depth -= 1
