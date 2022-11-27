"""
二叉排序树
设X是二叉树的一个节点，如果y是x的左子树，那么y.val<= x.val,如果y是x的右子树，那么y.val=> x.val
"""

from binary_tree import TreeNode, in_order, pre_order, post_order, level_order


class BST:

    def __init__(self, li=None):
        self.root = None
        if li is not None:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, value):
        if node is None:
            # 空树
            node = TreeNode(value)
        elif value < node.val:
            self.insert(node.left, value)
        elif value > node.val:
            self.insert(node.right, value)
        return node

    def insert_no_rec(self, value):
        p = self.root
        if p is None:
            self.root = TreeNode(value)
            return
        while True:
            if value < p.val:
                if p.left:
                    p = p.left
                else:
                    p.left = TreeNode(value)
                    return
            elif value > p.val:
                if p.right:
                    p = p.right
                else:
                    p.right = TreeNode(value)
                    return
            else:
                return


if __name__ == '__main__':
    tree = BST([3, 4, 9, 13, 8, 7, 9, 15])
    in_order(tree.root)
