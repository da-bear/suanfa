# TODO: 105. 根据前序遍历和中序遍历的结果还原一棵二叉树 ==> (!!! 假设树中没有重复的元素)

# 前序序列：E,A,C,B,D,G,F |  中序序列： A,B,C,D,E,G,F  ==> 还原二叉树
# 分析:   前序序列的第一个节点是根节点， 在中序序列中根节点的左侧是左子树，右侧是右子树， 如A是E的左节点
#         前序序列中若A的下一个节点C在中序序列A的右侧则是C是A的右节点


# 定义二叉树的节点
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree(pre_order, in_order):
    """
    :param pre_order: 二叉树的前序序列List[int]
    :param in_order:  二叉树的中序序列List[int]
    :return: 重建的二叉树的根节点
    """
    # 根节点
    if pre_order and in_order:
        node = TreeNode(pre_order[0])
        node_index = in_order.index(node.value)

        # 重建左子树
        node.left = build_tree(pre_order[1:node_index + 1], in_order[:node_index])
        # 重建右子树
        node.right = build_tree(pre_order[node_index + 1:], in_order[node_index + 1:])

        return node


def pre_order_check(node):
    if node:
        print(node.value, end=",")
        pre_order_check(node.left)
        pre_order_check(node.right)


def in_order_check(node):
    if node:
        in_order_check(node.left)
        print(node.value, end=",")
        in_order_check(node.right)


if __name__ == '__main__':
    p_order = [3, 9, 20, 15, 7]
    i_order = [9, 3, 15, 20, 7]

    A = build_tree(p_order, i_order)
    pre_order_check(A)
    print(end="----------")
    in_order_check(A)
