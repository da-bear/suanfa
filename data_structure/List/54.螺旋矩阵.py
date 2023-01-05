"""
题目：
    给你一个m行n列的矩阵matrix，请按照顺时针的顺序，返回矩阵中的所有元素
        1 -> 2 -> 3 -> 4
        5 -> 6 - >7    8
        9<-10<- 11 <- 12

分析：
    解题的核心思路是按照右、 下、 左、 上的顺序遍历数组，并使用四个变量圈定未遍历元素的边界
"""


def spiralOrder(matrix):
    res = []
    m = len(matrix)  # 行数
    n = len(matrix[0])  # 列数
    # left,right,top,bottom 为未遍历元素的边界
    left = top = 0
    right = n - 1
    bottom = m - 1

    while len(res) < m * n:
        # 从左往右遍历
        if top <= bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
        # 从上到下遍历
        if left <= right:
            for j in range(top, bottom):
                res.append(matrix[j][right])
            right -= 1
        # 从右到左遍历
        if top <= bottom:
            for k in range(left, right, -1):
                res.append(matrix[bottom][k])
            bottom -= 1
        # 从下到上遍历
        if left <= right:
            for t in range(top, bottom, -1):
                res.append(matrix[t][left])
            left += 1

    return res













