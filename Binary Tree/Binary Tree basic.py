# 2021-04-08
# 二叉树的创建 & 遍历
from collections import deque


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
f = TreeNode("F")
g = TreeNode("G")

e.left = a
e.right = g
a.right = c
c.left = b
c.right = d
g.right = f

root = e


# 访问root的左节点的右节点
# print(root.left.right.value)

# 前序遍历：先访问根节点，在访问左子树，再访问右子树
def pre_order(node):
    if node:
        print(node.value, end=",")
        pre_order(node.left)
        pre_order(node.right)


# pre_order(root)     # E,A,C,B,D,G,F,

# 中序遍历：先遍历左子树，在访问自己，在遍历右子树
def in_order(node):
    if node:
        in_order(node.left)
        print(node.value, end=",")
        in_order(node.right)


# in_order(root)  # A,B,C,D,E,G,F


# 后续遍历:先遍历左子树，再遍历右子树，最后访问根节点
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value, end=",")


# post_order(root)

# 层序遍历 (按照树的层去遍历)
def level_order(node):
    queue = deque()
    queue.append(node)
    while len(queue) > 0:
        curr_node = queue.popleft()
        print(curr_node.value, end=",")
        if curr_node.left:
            queue.append(curr_node.left)
        if curr_node.right:
            queue.append(curr_node.right)


level_order(root)
