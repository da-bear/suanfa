"""
    todo：⚠️  ！！ 明确递归函数的定义，并且要相信递归函数 ！！ ⚠️
"""

"""
    题目：给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行
    输入: rowIndex = 3
    输出: [1,3,3,1]    
"""


def getRow(self, rowIndex: int):
    # 每一行的开头是1
    res = [1]
    if rowIndex == 0:
        return res
    # 获取上一行的res
    preRow = self.getRow(rowIndex - 1)
    # 将上一行每两个元素相加
    for i in range(len(preRow) - 1):
        res.append(preRow[i] + preRow[i + 1])

    # 每一行的结尾是1
    res.append(1)
    return res
