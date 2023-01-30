"""
给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
"""

from collections import deque


def levelOrderBottom(root):
    res1 = []
    queue = deque()
    if root is None:
        return res1
    # 放入根结点 -> 第一层
    queue.append(root)
    # 队列不空
    while len(queue) > 0:
        # 放置每一层的元素
        tmp = []
        for _ in range(len(queue)):
            p = queue.popleft()
            tmp.append(p.val)
            if p.left is not None:
                queue.append(p.left)
            if p.right is not None:
                queue.append(p.right)
        res1.append(tmp)
    return res1[::-1]
