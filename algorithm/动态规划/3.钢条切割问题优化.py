"""
动态规划

递归算法由于重复求解额相同的子问题效率极低
动态规划的思想
    每个子问题只求解一次，保存求解结果
    之后需要此问题时，只需查找保存的结果

时间复杂度 O(n2)

如何修改动态规划的算法，使其不仅输出最优解，还需输出最优的切割方案
对于每个子问题，保存切割一次时左边切下的长度

动态规划问题的关特征
    最优子结构  （有递推式）
        原问题的最优解中涉及多少个子问题
        在确定最优解使用哪些子问题时，需要考虑多少种选择
    重叠子问题



"""

from base_file.cal_time import timeit

p0 = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


@timeit
def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]


def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0
        res_s = 0
        for j in range(1, i + 1):
            if p[j] + r[i - j] > res_r:
                res_r = p[j] + r[i - j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s


def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    res = []
    while n > 0:
        res.append(s[n])
        n -= s[n]
    return s, res, r


print(cut_rod_dp(p0, 9))
print(cut_rod_solution(p0, 9))
