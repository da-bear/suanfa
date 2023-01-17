"""
题目：
    给你一个字符串 s 和一个整数 k，请你找出 s 中的最长子串，要求该子串中的每一 字符出现次数都不少于k。返回这一子串的长度。
    输入：s = "aaabb", k = 3
    输出：3
    解释：最长子串为 "aaa"，其中 'a' 重复了 3 次

    1 <= s.length <= 104
    s 仅由小写英文字母组成
    1 <= k <= 105

分析：
    s中的最长子串, 要求子串中的每个的字符出现次数都不少于k
    如果使用滑动窗口算法
    1、什么时候应该扩大窗口？
        如果窗口中的有些字符数量不满足k，则需要一致扩大窗口，但是不知到啥时候啥时候收缩窗口
        todo： 理论上讲，这种情况就不能用滑动窗口模板了，但有时候我们可以自己添加一些约束，来进行窗口的收缩
        题目说让我们求每个字符都出现至少 k 次的子串，我们可以再添加一个约束条件：求每个字符都出现至少 k 次，仅包含 count 种不同字符的最长子串。
    2、什么时候应该缩小窗口？
    3、什么时候得到一个合法的答案？
    ｜｜
    ｜｜
    1、什么时候应该扩大窗口？   窗口中字符种类小于 count 时扩大窗口。
    2、什么时候应该缩小窗口？   窗口中字符种类大于 count 时扩大窗口。
    3、什么时候得到一个合法的答案？窗口中所有字符出现的次数都大于等于 k 时，得到一个合法的子串。

    当然，题目没有 count 的约束，那没关系呀，count能有几种取值？
        因为 s 中只包含小写字母，所以 count 的取值也就是 1~26，所以最后用一个 for 循环把这些值都输入
        logestKLetterSubstr 计算一遍，求最大值就是题目想要的答案了。这充分体现了前文 我的刷题经验总结中所说：
        todo:算法的本质是穷举。

"""


def longestSubstring(s, k):
    """
    至少有 K 个重复字符的最长子串
    """
    length = 0
    for i in range(1, 27):
        length = max(length, longestKLetterSubstr(s, k, i))
    return length


def longestKLetterSubstr(s, k, count):
    """
    :param s: 目标字符串
    :param k: 字符重复数k
    :param count: 窗口中的字符种类限制
    :return:
    """
    # 窗口指针
    left = right = 0
    # 记录答案
    res = 0
    # 列表list存储字符字符出现次数
    windowCharCount = [0 for _ in range(26)]
    # 窗口中的字符种类 > count 时候缩小窗口
    windowCharCategory = 0
    # 记录窗口中有几种字符的出现次数达标（大于等于k）
    windowValidCount = 0

    while right < len(s):
        c = s[right]
        if windowCharCount[ord(c) - ord("a")] == 0:
            # 新增一种字符
            windowCharCategory += 1
        # 该字符数加1
        windowCharCount[ord(c) - ord("a")] += 1
        # 如果字符数等于k
        if windowCharCount[ord(c) - ord("a")] == k:
            windowValidCount += 1

        right += 1

        while windowCharCategory > count:
            d = s[left]
            if windowCharCount[ord(d) - ord("a")] == k:
                windowValidCount -= 1
            windowCharCount[ord(d) - ord("a")] -= 1
            # 窗口中的字符少一种
            if windowCharCount[ord(d) - ord("a")] == 0:
                windowCharCategory -= 1

            left += 1
        # 当窗口中字符种类为 count 且每个字符出现次数都满足 k 时，更新答案
        if windowValidCount == count:
            res = max(res, right - left)

    return res

















