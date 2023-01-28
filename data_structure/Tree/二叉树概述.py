"""
    todo:二叉树的问题就是一个二叉树的遍历问题

    1. 递归函数可以理解为一个指针, 一个在二叉树上游走的指针
    2. 前、中、后序是三个特殊的时间点
        - 前 -> 刚进入函数，没有递归左右子树时候，
        - 中 -> 递归遍历了左子树后，准备开始遍历右子树
        - 后 -> 左右子树都遍历完后
    3. 二叉树遍历算法需要思考的两个问题
        -  当前的节点需要去做什么事情
        -  应该在什么时候做这件事情
        理解：
    4. 二叉树算法的两大分类
        这两类思路分别对应着 回溯算法核心框架 和 动态规划核心框架。
"""


# 二叉树的节点
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 二叉树的遍历框架
def traverse(root):
    if root is None:
        return
    # 前序遍历的位置
    traverse(root.left)
    # 中序遍历的位置
    traverse(root.right)
    # 后续遍历的位置