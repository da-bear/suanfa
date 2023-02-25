"""
给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。
"""

from collections import deque


def largestValues(root):
    res = []
    if root is None:
        return res
    q = deque()
    q.append(root)
    while len(q) > 0:
        levelMax = - 2 ** 31
        for _ in range(len(q)):
            node = q.popleft()
            levelMax = max(levelMax, node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        res.append(levelMax)
    return res
