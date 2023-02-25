"""
    BFS：（广度优先）二叉树的层序遍历
    todo：⚠️ 优势：计算二叉树的最小深度不需要全部遍历二叉树 ，求最小值时候的效率较高
"""

from collections import deque


def level_order(root):
    res = []
    queue = deque()
    if root is None:
        return res
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
        res.append(tmp)
    return res
