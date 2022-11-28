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

    def query(self, node, val):
        if not node:
            return None
        if node.val > val:
            self.query(node.left, val)
        elif node.val < val:
            self.query(node.right, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.val > val:
                p = p.left
            elif p.val < val:
                p = p.right
            else:
                return p

        return None

    def delete(self, val):
        """
        假设要删除的节点q、 其父节点为p
            *** 如果被删节点是根结点， 需要做特殊处理
            1 - 通过val找到节点p、父节点q
            2 - 删除节点，不同的情形
                - 如果q是叶子节点， 则将p对q的引用指向为None
                - 如果q不是叶子节点， 需要将q的子树链接到删除q之后的树中
                    - 如果 q 没有左子树，将q的右子树改为p的左子树
                    - 如果 q 有左子树， 需要找到q左子树的最右节点 r （左子树中的最大值）
                        - 用q的左子节点作为p的左子节点
                        - 用q的右子树作为r的右子树
        """
        p, q = None, self.root

        # 删除节点为q， 父节点q
        while q and q.val != val:
            p = q
            if val < q.val:
                q = q.left
            else:
                q = q.right

        if q is None:
            return

        if q.left is None:
            if p is None:  # q是根节点
                self.root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return

        r = q.left
        while r.right:
            r = r.right

        r.right = q.right
        if p is None:
            self.root = q.left  # q是根结点

        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left


if __name__ == '__main__':
    tree = BST([10, 3, 4, 9, 13, 8, 7, 9, 15])
    in_order(tree.root)
