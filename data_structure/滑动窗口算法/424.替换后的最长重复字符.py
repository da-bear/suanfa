"""
题目：
    给你一个字符串s和一个整数k，你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字，改操作最多可执行k次
    在执行上述操作后，返回包含相同字母的最长子字符串长度

    输入：s = "ABAB", k = 2
    输出：4
    解释：用两个'A'替换为两个'B',反之亦然。


    输入：s = "AABABBA", k = 1
    输出：4
    解释：
    将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
    子串 "BBBB" 有最长重复字母, 答案为 4。

    1 <= s.length <= 105
    s 仅由大写英文字母组成
    0 <= k <= s.length

分析：使用滑动窗口算法
    1、什么时候应该扩大窗口？
        当可替换次数大于0时，扩大窗口，所有进入窗口的字符都进行替换，使得窗口内的所有元素都是重复的。
    2、什么时候应该缩小窗口？
        当可替换次数小于0时，缩小窗口，空余出更多可替换次数，以便之后继续扩大窗口。
    3、什么时候得到一个合法的答案？
        只要可替换次数大于等于 0，窗口中的字符串都是重复的，我们想求的是一个最大窗口长度。
"""


def characterReplacement(s, k):
    """
    :param s: 输入字符串s
    :param k: 更改次数k
    :return: 最长子串的长度
    """
    left = right = 0
    # 列表记录窗口中出现的大写字母的个数
    windowCharCount = [0 for _ in range(26)]
    # 窗口最大的重复字母数
    windowMaxCount = 0

    # 结果长度
    res = 0
    while right < len(s):
        c = s[right]
        # 计算窗口中c的个数
        windowCharCount[ord(c) - ord("A")] += 1
        windowMaxCount = max(windowMaxCount, windowCharCount[ord(c) - ord("A")])
        right += 1

        # 可替换次数大于k则缩小窗口
        while right - left - windowMaxCount > k:
            d = s[left]
            windowCharCount[ord(d) - ord("A")] -= 1
            left += 1

        res = max(res, right - left)

    return res




