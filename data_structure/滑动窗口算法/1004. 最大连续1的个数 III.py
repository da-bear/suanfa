"""
题目：
    给定一个二进制数组 nums 和一个整数 k，如果最多可以把 k 个 0 翻转成 1，请返回数组中连续 1 的最大个数
        输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
        输出：6
        解释：[1,1,1,0,0,1,1,1,1,1,1]
        把 2 两个 0 翻转成 1，最长的值为 1 的子数组长度为 6。
分析：
    可以维护一个窗口在nums上滑动，保证nums中所有的数字都被替换成1，那么窗口可以达到的最大程度就是答案
"""


def longestOnes(nums, k):
    left = right = 0
    window_one_count = 0
    res = 0
    while right < len(nums):
        if nums[right] == 1:
            window_one_count += 1
        right += 1

        while right - left - window_one_count > k:
            # 当窗口中需要替换的0的数量大于k，缩小窗口
            if nums[left] == 1:
                window_one_count -= 1
            left += 1
        # 此时一定是一个合法的窗口，求最大窗口长度
        res = max(res, right - left)

    return res

