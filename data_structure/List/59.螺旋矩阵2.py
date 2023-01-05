"""
题目：
    给你一个正整数n，生成一个包含1 - n**2所有元素，切元素按顺时针的顺序螺旋排列成nxn
    的正方形矩阵matrix
"""


def generateMatrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    top = left = 0
    right = bottom = n - 1

    num = 0  # 填入矩阵中的数
    while num < n ** 2:
        # 从左向右遍历填充
        if top < bottom:
            for i in range(left, right):
                num += 1
                matrix[top][i] = num
            top += 1

        if left < right:
            for j in range(top, bottom):
                num += 1
                matrix[j][right] = num
            right -= 1

        if top < bottom:
            for k in range(left, right, -1):
                num += 1
                matrix[bottom][k] = num
            bottom -= 1

        if left < right:
            for t in range(top, bottom, -1):
                num += 1
                matrix[t][left] = num
            left += 1

    return matrix


