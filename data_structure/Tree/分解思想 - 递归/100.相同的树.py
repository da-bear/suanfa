"""
    todo：⚠️  ！！ 明确递归函数的定义，并且要相信递归函数 ！！ ⚠️
"""

"""
    题目：
        给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
        如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的
"""


def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
