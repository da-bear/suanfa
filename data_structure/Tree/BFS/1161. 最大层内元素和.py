"""
题目：
    给你一个二叉树的根节点 root。
    设根节点位于二叉树的第1层，而根节点的子节点位于第2层，依此类推。
    请返回层内元素之和最大的那几层（可能只有一层）的层号，并返回其中最小的那个。

    输入：root = [1,7,0,7,-8,null,null]
    输出：2
    解释：
    第 1 层各元素之和为 1，
    第 2 层各元素之和为 7 + 0 = 7，
    第 3 层各元素之和为 7 + -8 = -1，
    所以我们返回第 2 层的层号，它的层内元素之和最大。
"""

from collections import deque


def maxLevelSum(root):
    if root is None:
        return -1
    maxSum = -10 ** 5
    depth = 0
    index = 0
    q = deque()
    q.append(root)
    while len(q) > 0:
        levelSum = 0
        for _ in range(len(q)):
            node = q.popleft()
            levelSum += node.val
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        depth += 1
        if levelSum > maxSum:
            maxSum = levelSum
            index = depth
    return index
