"""
题目
    给你一个包含 若干 单词 和空格的字符串s，请你写一个算法，原地反转所有的单词的顺序

分析：
    eg：s = "hello world" =>  需要原地反转  => "world hello"
    常规的方式是把s按空格 split成若干 单词，然后 reverse 这些单词的顺序，最后把这些单词 join 成句子。
    但这种方式使用了额外的空间，并不是「原地反转」单词。

    1 - 先将整个字符串s反转： s = "dlrow olleh"
    2 - 将每个单词反转    s = "world hello"
"""


def reverseWords_1(s):
    return ''.join(reversed(s.split()))


def trim_space(s):
    """
    去除空白
    """
    left, right = 0, len(s) - 1
    # 去掉字符串开头的空白字符
    while left <= right and s[left] == " ":
        left += 1

    # 去掉字符串末尾的空白字符
    while left <= right and s[right] == " ":
        right -= 1

    # 将字符串间多余空白字符去除
    output = []
    while left <= right:
        if s[left] != " ":
            output.append(s[left])
        elif output[-1] != " ":  # 单词之间只留一个空格
            output.append(s[left])
        left += 1

    return output


def reserve(s, left, right):
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return s


def reserveWorlds(s):
    # 将字符串去除两端空格，返回组成的列表
    l = trim_space(s)
    # 将字符串s全部进行反转
    l = reserve(l, 0, len(l) - 1)
    # 将以空格为分隔的单词reserve

    start = end = 0
    n = len(l)
    while start < n:
        while end < n and l[end] != " ":
            end += 1
        # 翻转单词
        reserve(l, start, end - 1)
        start = end + 1
        end += 1

    return ''.join(l)


if __name__ == '__main__':
    a = "    hello      world     but     "
    # print(reserve(a))

    print(reserveWorlds(a))
