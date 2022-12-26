"""
二叉树、树：
    二叉排序树：二叉搜索树
    平衡二叉树：AVL树
    完全二叉树：优先队列
    动态多分支排序树：
"""
from collections import deque


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# 前序遍历： 节点 -> 左子树 -> 右子树
def pre_order(node):
    if node is not None:
        print(node.val, end=",")
        pre_order(node.left)
        pre_order(node.right)


# 中序遍历: 左子树 -> 节点 -> 右子树
def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.val, end=",")
        in_order(node.right)


# 后序遍历：左子树 -> 右子树 -> 节点
def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.val, end=",")


def level_order(root):
    # 创建队列
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.val, end=",")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# 如果把根节点看做第 1 层，如何打印出每一个节点所在的层数？
def traverse(node, level):
    if node is None:
        return
    print("node %s 在%s层" % (node.val, level))
    traverse(node.left, level + 1)
    traverse(node.right, level + 1)


# 如何打印出每个节点的左右子树各有多少节点？
def count_node(node):
    if node is None:
        return 0
    left_count = count_node(node.left)
    right_count = count_node(node.right)
    print("node %s left-count %s, right-count %s" % (node.val, left_count, right_count))

    return left_count + right_count + 1


if __name__ == '__main__':
    a = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")
    g = TreeNode("G")

    e.left = a
    e.right = g
    g.right = f
    a.right = c
    c.left = b
    c.right = d

    root = e

    # print(root.val)
    # print(root.right.val)

    # pre_order(root)
    # level_order(root)
    # traverse(root, 1)
    count_node(root)
