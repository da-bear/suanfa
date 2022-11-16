# TODO: 102. 二叉树的层序遍历


from collections import deque


def level_order(node):
    res = []
    queue = deque()
    queue.append(node)
    while len(queue) > 0:
        current_node = queue.popleft()
        if current_node.value:
            res.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return res


def level_order_2(node):
    res = []
    if not node:
        return res
    queue = deque()
    queue.append(node)
    while queue:
        tmp = []
        for _ in range(len(queue)):
            current_node = queue.popleft()
            if current_node:
                tmp.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        res.append(tmp)

    return res
#   return res[::-1]   给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）






















