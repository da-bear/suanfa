"""
    todo：⚠️  ！！ 明确递归函数的定义，并且要相信递归函数 ！！ ⚠️
"""

"""
    题目：给定一个二叉树，找出其最小深度。
        最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
        说明：叶子节点是指没有子节点的节点。   
"""


def minDepth(self, root):
    if root is None:
        return 0
    left_depth = self.minDepth(root.left)
    right_depth = self.minDepth(root.right)
    # 如果左右子树有一个为空， 则最小深度为不空的子树的最小高度+ 1
    if root.left is None or root.right is None:
        return left_depth + right_depth + 1
    return min(left_depth, right_depth) + 1
