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
