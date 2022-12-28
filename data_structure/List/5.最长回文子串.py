"""
题目：
    给你一个字符串s，找到s中最长的 回文子串。如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

分析：
    如何判断回文串?
        首先明确一下，回文串就是正着读和反着读都一样的字符串。比如说字符串aba和abba都是回文串,
        因为它们对称，反过来还是和本身一样；反之，字符串 abac 就不是回文串。

    找回文串的难点在于,回文串的的长度可能是奇数也可能是偶数,
    解决该问题的核心是从中心向两端扩散的双指针技巧。


注意：
    最长回文子串使用的 左右 指针 和之前题目的左右指针有一些不同：
    之前的左右指针都是从两端向中间相向而行，而回文子串问题则是让左右指针从中心向两端扩展。
    不过这种情况也就回文串这类问题会遇到，所以我也把它归为左右 指针了。
"""


def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def palindrome(s, l, r):
    """
    在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串
    """
    while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
        l -= 1
        r += 1

    return s[l + 1: r]


def longestPalindrome(s):
    """
    :param s: str
    :return: longest palindrome str
    """
    res = ""
    for i in range(len(s)):
        # 获取以 s[i] 为中心的回文串
        s1 = palindrome(s, i, i)
        # 获取以 s[i], s[i+1] 为中心的回文串
        s2 = palindrome(s, i, i+1)

        res = s1 if len(s1) > len(res) else res
        res = s2 if len(s2) > len(res) else res

    return res