"""
题目：给定两个字符串s和p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序
    异位词: 指由相同字母重新排列形成的字符串

分析：
    相当于，输入一个串 S，一个串 T，找到 S 中所有 T 的排列，返回它们的起始索引
"""


def findAnagrams(s, p):
    window = dict()
    target = dict()
    for c in p:
        target[c] = target.get(c, 0) + 1

    left = right = 0
    valid = 0
    # 索引列表
    res = []
    while right < len(s):
        # 向右滑动
        c = s[right]
        right += 1
        if target.get(c, 0):
            window[c] = window.get(c, 0) + 1
            if window[c] == target[c]:
                valid += 1

        # 窗口收缩的条件
        while right - left >= len(p):
            if valid == len(target):
                res.append(left)
            d = s[left]
            left += 1
            if target.get(d, 0):
                if window[d] == target[d]:
                    valid -= 1
                window[d] -= 1
    return res
