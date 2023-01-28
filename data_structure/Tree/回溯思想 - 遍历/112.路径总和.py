"""
题目：
    给你二叉树的根节点 root 和一个表示目标和的整数 targetSum。
    判断该树中是否存在 根节点到叶子节点的路径，
    这条路径上所有节点值相加等于目标和 targetSum 。
    如果存在，返回 true；否则，返回 false。
"""


class Solution:
    def __init__(self):
        self.found = False
        self.curSum = 0

    def hasPathSum(self, root, targetSum):
        self.traverse(root, targetSum)
        return self.found

    def traverse(self, node, target):
        if node is None or self.found:
            return
        self.curSum += node.val
        if node.left is None and node.right is None:
            if self.curSum == target:
                self.found = True
        self.traverse(node.left, target)
        self.traverse(node.right, target)
        self.curSum -= node.val