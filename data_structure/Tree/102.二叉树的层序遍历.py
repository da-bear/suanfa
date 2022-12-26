"""
二叉树的层序遍历
"""

from collections import deque
from binary_tree import root


def level_order(node):
    res = []
    queue = deque()
    queue.append(node)
    if node is None:
        return res
    while len(queue) > 0:
        tmp = []
        for _ in range(len(queue)):
            node = queue.popleft()
            tmp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(tmp)
    return res


if __name__ == '__main__':
    print(level_order(root))
