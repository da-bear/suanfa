"""
题目：
    请你实现一个函数，接受一个正整数n，函数能够打印所有长度为 n 的二进制数。
    例如输入n = 3，算法打印000 001 010 011 100 101 110 111，共2^3 = 8个结果。
    函数签名如下  generateBinaryNumber
    ps: 如果是所有长度为n的十进制数
"""

path = ""


def generateBinaryNumber(n):
    global path
    if n == 0:
        # n = 0 时候输出path
        print(path)
        return

    # 二进制
    for i in range(10):
        # for 循环中的前序遍历会忽略根结点
        path += str(i)
        generateBinaryNumber(n - 1)
        path = path[:-1]


if __name__ == '__main__':
    generateBinaryNumber(2)
