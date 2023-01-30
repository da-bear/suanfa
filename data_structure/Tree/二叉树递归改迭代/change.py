"""
    二叉树递归算法改迭代算法
    考察：对递归过程的理解
    二叉树的递归过程：-> 函数的执行过程
        前序位置元素放入栈， 后续位置（离开节点的以后）出栈
    迭代遍历框架
    todo: 核心：不要让系统的递归调用栈处理递归逻辑，我们自己用栈模拟递归的逻辑，区分出什么什么时候进行前、中、后序的位置
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.stk = []

    # 左子树一直到底
    def pushLeftBranch(self, node):
        while node is not None:
            # todo:前序遍历的代码位置
            self.stk.append(node)
            node = node.left

    def traverse(self, root):
        # 指向上一次遍历完的子树的根点(出栈的元素)
        visited = TreeNode(-1)
        # 开始遍历整棵树
        self.pushLeftBranch(root)

        while len(self.stk) > 0:
            # 栈中的最后一个元素（最左子节点）
            p = self.stk[-1]

            # p的左子树遍历完成了，且右子树没有遍历
            if (p.left is None or p.left == visited) and p.right != visited:
                # todo: 中序遍历代码位置
                # 遍历p的右子树
                self.pushLeftBranch(p.right)

            # p的右子树遍历完了
            if p.right is None or p.right == visited:
                # todo 后续遍历位置
                # 以p为根节点的子树被遍历完成了，出栈visited指向p
                visited = self.stk.pop()


