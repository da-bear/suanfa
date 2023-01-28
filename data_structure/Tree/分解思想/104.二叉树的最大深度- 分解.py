"""
    todo：⚠️  ！！ 明确递归函数的定义，并且要相信递归函数 ！！ ⚠️
"""

"""
题目：
    给定一个二叉树，找出其最大深度
    二叉树的深度为根结点到最圆叶子节点的最长路径上的节点数
"""


def max_depth(node):
    """
    只要明确递归函数的定义，这个解法也不难理解，但为什么主要的代码逻辑集中在后序位置？
    因为这个思路正确的核心在于，你确实可以通过子树的最大深度推导出原树的深度，
    所以当然要首先利用递归函数的定义算出左右子树的最大深度，然后推出原树的最大深度，主要逻辑自然放在后序位置。
    """
    if node is None:
        return 0
    left_max = max_depth(node.left)
    right_max = max_depth(node.right)
    return max(left_max, right_max) + 1


