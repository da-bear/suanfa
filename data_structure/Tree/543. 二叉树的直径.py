"""
给定一棵二叉树，你需要计算它的直径长度
一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。


解题目的关键
    每一条二叉树的「直径」长度，就是一个节点的左右子树的最大深度之和
    求整棵树中的最长直径，可以遍历整棵树中的每个节点，随后通过每个节点的左右子树的最大深度计算出每个节点的直径，最后将每个直径求最大值即可
"""
from binary_tree import TreeNode

max_diameter = 0


def diameter(node):
    max_depth(node)
    return max_diameter


def max_depth(node):
    """
    计算节点的最大深度
    """
    if node is None:
        return 0
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)
    global max_diameter
    mode_depth = left_depth + right_depth
    max_diameter = max(mode_depth, max_diameter)
    return max(left_depth, right_depth) + 1


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

    print(diameter(root))
