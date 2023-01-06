"""
题目：
    给你两个字符串s1和s2，写一个函数来判断s2是否包含s1的排列，如果是，返回true，否则，返回false
    即：s1的排列之一 是s2的子串

分析：
    滑动窗口算法: 相当给你一个 S 和一个 T，请问你 S 中是否存在一个子串,包含T中所有字符且不包含其他字符
"""


def checkInclusion(s1, s2):
    """
    判断s2中是否存在一个子串，子串包含s1中的所有字符，且不包含其他字符
    """
    window = dict()
    target = dict()
    for c in s1:
        target[c] = target.get(c, 0) + 1

    left = right = 0
    valid = 0
    while right < len(s2):
        # 向右滑动
        c = s2[right]
        right += 1
        if target.get(c, 0):
            window[c] = window.get(c, 0) + 1
            if window[c] == target[c]:
                valid += 1

        # 判断窗口是否要收缩 (本题移动 left 缩小窗口的时机是窗口大小大于 t.size() 时，因为排列嘛，显然长度应该是一样的)
        while right - left >= len(s1):
            if valid == len(target):
                return True
            d = s2[left]
            left += 1
            if target.get(d, 0):
                if window[d] == target[d]:
                    valid -= 1
                window[d] -= 1
    return False





