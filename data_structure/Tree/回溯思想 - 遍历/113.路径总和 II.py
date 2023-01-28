"""
题目：
    给你二叉树的根节点 root 和一个整数目标和 targetSum ，
    找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
    叶子节点 是指没有子节点的节点。
"""
import copy


class Solution:
    def __init__(self):
        self.res = []
        self.curSum = 0
        self.pathRes = []

    def pathSum(self, root, targetSum):
        self.traverse(root, targetSum)
        return self.res

    def traverse(self, node, targetSum):
        if node is None:
            return
        self.curSum += node.val
        self.pathRes.append(node.val)
        if node.left is None and node.right is None:
            if self.curSum == targetSum:
                self.res.append(copy.deepcopy(self.pathRes))
        self.traverse(node.left, targetSum)
        self.traverse(node.right, targetSum)

        self.curSum -= node.val
        self.pathRes.pop()
