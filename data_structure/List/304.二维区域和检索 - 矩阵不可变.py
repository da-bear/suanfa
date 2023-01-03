"""
题目：
    给定一个二维矩阵 matrix，以下类型的多个请求：
    计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1, col1) ，右下角 为 (row2, col2) 。
实现 NumMatrix 类：
    NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
    int sumRegion(int row1,int col1,int row2,int col2) 返回左上角 (row1,col1)、右下角 (row2,col2)所描述的子矩阵的元素总和 。
"""


class NumMatrix:

    def __init__(self, matrix):
        self.pre_sum = self.init_sum(matrix)

    @staticmethod
    def init_sum(matrix):
        """
        定义：preSum[i][j] 记录 matrix 中子矩阵 [0, 0, i-1, j-1] 的元素和
        """
        m = len(matrix)  # 行
        n = len(matrix[0])  # 列
        if m == 0 or n == 0:
            return matrix
        pre_sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 计算每个矩阵[0, 0, i, j]的元素和
                pre_sum[i][j] = pre_sum[i-1][j] + pre_sum[i][j - 1] - pre_sum[i-1][j-1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int):
        return self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row1][col2 + 1] - self.pre_sum[row2 + 1][col1] + self.pre_sum[row1][col1]
