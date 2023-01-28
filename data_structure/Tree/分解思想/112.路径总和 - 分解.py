"""
题目：
    给你二叉树的根节点 root 和一个表示目标和的整数 targetSum。
    判断该树中是否存在 根节点到叶子节点的路径，
    这条路径上所有节点值相加等于目标和 targetSum 。
    如果存在，返回 true；否则，返回 false。
"""


def hasPathSum(root, targetSum):
    if root is None:
        return False
    if root.left == root.right:
        return root.val == targetSum
    return hasPathSum(root.left, targetSum-root.val) or hasPathSum(root.right, targetSum- root.val)
