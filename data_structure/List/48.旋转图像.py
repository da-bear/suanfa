"""
题目：
    给定一个nxn的二维矩阵matrix表示一个图像，清你讲图像顺时针旋转90度
    你必须在 原地 旋转图像，这一位置额你要直接修改输入的二维矩阵，请不要使用另一个矩阵来旋转图像

     1  2   3                    7   4   1
     4  5   6      =》           8   5   2
     7  8   9                    9   6   3

    输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
    输出：[[7,4,1],[8,5,2],[9,6,3]]

分析：
    如何「原地」旋转二维矩阵？稍想一下,感觉操作起来非常复杂,可能要设置巧妙的算法机制来「一圈一圈」旋转矩阵

    常规思路：
        寻找原始坐标和旋转坐标的映射规律，但我们时候可以让思维跳跃，尝试将矩阵进行反转，镜像对称操作
"""


def rotate_1(matrix):
    """
    将二维矩阵matrix顺时针原地旋转90度
    """
    # 先将二维矩阵沿着左上右下的对角线做镜像对称
    n = len(matrix)  # 行，由于是N x N 的矩阵
    for i in range(n):
        for j in range(i, n):  # 遍历对角线的一般就可以
            # swap (matrix[i][j], matrix[j][i])
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for l in matrix:
        reserve(l)


def rotate_2(matrix):
    """
    将二维矩阵matrix 逆时针原地旋转90度
    """
    # 先将二维矩阵沿着左上右下的对角线做镜像对称
    n = len(matrix)  # 行，由于是N x N 的矩阵
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]

    for l in matrix:
        reserve(l)


def reserve(l):
    left = 0
    right = len(l) - 1
    while left < right:
        l[left], l[right] = l[right], l[left]
        left += 1
        right -= 1
    return l
