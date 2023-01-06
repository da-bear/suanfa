"""
题目：
    给你一个字符串s、一个字符串t。
    返回s中涵盖t所有字符的最小子串。如果s中不存在涵盖t所有字符的子串，则返回空字符串 ""

    注意：
        对于t中重复字符，我们寻找的子字符串中该字符数量必须不少于t中该字符数量
        如果s中存在这样的字符，我们保证它是唯一的答案

    提示：
        m== s.length
        n== t.length
        1 <= m, n <= 10**5
    进阶：如何设计一个在O(m + n) 时间内解决此问题


分析：
    1 - 我们在字符串 s 中使用双指针的左右指针技巧，初始化left = right = 0, 将索引左闭右开区间 [left,right) 称为一个窗口
            这样处理的好处是：初始化left = right = 0 区间[0,0)中没有元素，只要将right向右移动一位[0, 1) 区间就包含一个元素
            如果设置了两端都开的区间,那么让right向右移动一位后（0， 1）任然没有元素
            如果设置了两端都闭的区间，初始区间[0,0]就包含了一个元素
            这两种情况都会给边界处理带来不必要的麻烦
    2 - 我们先不断增加right指针扩大窗口【left， right），知道窗口中的字符串符合要求（包含了T中所有的字符）
    3 - 此时停止增加right，转而不断增加left指针缩小矿口[left, right), 直到窗口中的字符串不再符合要求
    （不包含T中的所有字符了），同时每次增加left，我们都要更新一轮结果

    4 - 重复第 2 步 和第3步，直到right到达字符串的 s 的尽头

    第2步 相当于寻找一个可行解，然后在第3步 再优化这个可行解，最终找到最优解也就是最短 的覆盖子串，左右 指针轮流前进，
    窗口大小增增减减，窗口不断向右滑动

思考：
    1 - 初始化window和need两个哈希表，记录窗口中的字符和需要凑齐的字符
    2 - 使用left 和 right 变量初始化窗口的两端，[left, right) 是左闭右开的，初始情况下窗口没有包含任何元素
        left = right = 0
        valid = 0
        while right < len(s):
            # 开始滑动
        其中valid 变量表示窗口中满足need条件的字符个数，如果valid和 need的size大小相同，
        则说明窗口已经满足条件，已经完全覆盖了T

    3 - 思考：
        什么时候应该移动right扩大窗口？窗口加入字符时，应该更新哪些数据？
        什么时候应该暂停扩大，开始移动left缩小窗口？从窗口移出字符时，应该更新哪些数据？
        我们要的结果应该在扩大窗口还是缩小窗口时进行更新？

        如果一个字符进入窗口，应该增加window计数器；如果一个字符移出窗口时候，应该减少window技术器；
        当valid满足need时应该收缩窗口，应该在收缩窗口时候更新最终结果
"""


def minWindow(s, t):
    """
    :param s:
    :param t:
    :return:
    """
    window = dict()
    need = dict()
    for c in t:
        need[c] = need.get(c, 0) + 1

    # 窗口区间
    left = right = 0
    # 最小覆盖子串的start 与length
    start = 0
    length = 10**5
    # 窗口中满足need条件的字符个数
    valid = 0

    while right < len(s):
        # 开始滑动，将c移入窗口
        c = s[right]
        right += 1
        if need.get(c):
            window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                # 如果c的个数满足
                valid += 1

        # 判断窗口左侧是否要收缩
        while valid == len(need):
            # 更新最小覆盖子串
            if right - left < length:
                start = left
                length = right - left
            # d 是将要移出窗口的字符
            d = s[left]
            left += 1
            if need.get(d):
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    return "" if length == 10**5 and s != t else s[start: start + length]


if __name__ == '__main__':
    minWindow("a", "a")
