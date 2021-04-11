# 二叉搜索树是一棵二叉树，且满足性质：
# 设X是二叉树的一个节点，如果y是x的左子树，那么y.val<= x.val,如果y是x的右子树，那么y.val=> x.val
import random


# 树的节点
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# 二叉搜索树的类
class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):
        if not node:
            # 空树
            node = TreeNode(val)
        elif val < node.value:
            node.left = self.insert(node.left, val)
            node.left.parent = node
        elif val > node.value:
            node.right = self.insert(node.right, val)
            node.right.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:  # 空树
            self.root = TreeNode(val)
            return
        while True:
            if val < p.value:
                if p.left:
                    p = p.left
                else:
                    p.left = TreeNode(val)
                    p.left.parent = p
                    return
            elif val > p.value:
                if p.right:
                    p = p.right
                else:
                    p.right = TreeNode(val)
                    p.right.parent = p
                    return
            else:
                return

    def pre_order(self, node):
        if node:
            print(node.value, end=",")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.value, end=",")
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=",")

    def query(self, node, val):
        if not node:
            return None
        if val < node.value:
            return self.query(node.left, val)
        elif val > node.value:
            return self.query(node.right, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if val < p.value:
                p = p.left
            elif val > p.value:
                p = p.right
            else:
                return p
        return None


if __name__ == '__main__':
    l1 = list(range(0, 300, 2))
    random.shuffle(l1)
    tree = BST(l1)
    # tree.pre_order(tree.root)
    # print("")
    # tree.in_order(tree.root)
    # print("")
    # tree.post_order(tree.root)
    # print(tree.query(tree.root, 4).value)
    # print(tree.query(tree.root, 17))
    # print(tree.query_no_rec(13))
