"""
    todo：⚠️  ！！ 明确递归函数的定义，并且要相信递归函数 ！！ ⚠️
"""

"""
    题目：
        给你二叉树的根结点 root ，请你将它展开为一个单链表：
        展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
        展开后的单链表应该与二叉树 先序遍历 顺序相同。
"""


def flatten(root) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if root is None:
        return
        # 将左、 右子树拉为链表
    flatten(root.left)
    flatten(root.right)

    # 暂存
    left = root.left
    right = root.right

    root.left = None
    root.right = left

    p = root
    while p.right is not None:
        p = p.right
    # 将链表拼回
    p.right = right