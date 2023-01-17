
"""
给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。
"""
def numSubarrayProductLessThanK(nums, k):
    left = right = 0
    # 窗口内数的乘积， 初始值为1
    windowProduct = 1
    # 符合条件的子数组个数
    cnt = 0
    while right < len(nums):
        windowProduct *= nums[right]
        right += 1

        while windowProduct >= k and left < right:
            windowProduct /= nums[left]
            left += 1
        cnt += right - left

    return cnt

