"""
最长公共子序列
一个序列的子序列是在该序列中删去若干元素后得到的序列
    eg： 'ABCD' 和 'BDF' 都是'ABCDEFG'的子序列

最长公共子序列（LCS）问题：给定两个序列X和Y，求X和Y长度最大的公共子序列
    eg：X = "ABBCBDE" Y="DBBCDB"

应用场景：字符串相似度比对

定理：（LCS的最优子结构）令 X = < x1, x2, .... xm> 和 Y = <y1, y2, ....,yn> 为
      两个序列， Z = <z1, z2, ... zk> 为X和Y的任意LCS
      1. 如果 xm = yn, 则zk = xm = yn 且Zk-1是 Xm-1和Yn-1的一个LCS
      2. 如果 xm != yn, 那么zk != xm, 意味着Z是Xm-1 和Y的一个LCS
      3. 如果 xm != yn, 那么zk != yn, 意味着Z是X和Yn-1的一个LCS

               {   0                            若 i=0 或 j=0
      c[i,j] = |   c[i-1, j-1] + 1              若i，j > 0 且 xi = yi
               {   max(c[i, j-1], c[i-1, j])    若i，j > 0 且 xi != yi

     c[i,j] 表示Xi和Yj的LCS长度
"""


def lcs_length(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[m][n]


def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # 位置上的字符匹配的时候，来自左上方
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i - 1][j] > c[i][j - 1]:  # 来自上方
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:  # 来自左方
                c[i][j] = c[i][j - 1]
                b[i][j] = 3

    return c[m][n], b


def lcs_traceback(x, y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:  # 来自左上方
            res.append(x[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:  # 来自上方
            i -= 1
        else:
            j -= 1
    return "".join(reversed(res))


print(lcs_traceback("ABCBDAB", "BDCABA"))
