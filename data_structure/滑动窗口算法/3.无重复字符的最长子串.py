"""
题目：
    给定一个字符串s，请找出其中不含有重复字符的最长子串
"""


def lengthOfLongestSubstring(s):
    left = right = 0
    window = dict()
    res = ''
    while right < len(s):
        c = s[right]
        right += 1
        window[c] = window.get(c, 0) + 1

        # 向右移动的条件是出现重复字符串
        while window[c] > 1:
            d = s[left]
            left += 1
            window[d] -= 1
        res = res if right - left < len(res) else s[left: right]

    return res


if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb"))
