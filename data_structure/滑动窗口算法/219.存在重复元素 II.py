"""
题目：
    给你一个整数数组nums和一个整数k，判断数组中是否存在两个不同的索引i和j，
    满足 nums[i] == nums[j] 且 abs(i - j) <= k。如果存在，返回true；否则，返回 false

    输入：nums = [1,2,3,1], k = 3
    输出：true

    输入：nums = [1,0,1,1], k = 1
    输出：true

    输入：nums = [1,2,3,1,2,3], k = 2
    输出：false

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109
    0 <= k <= 105

分析：
    维护一个大小为k窗口， 滑动过程中计算是否存在有重复元素
    1、什么时候应该扩大窗口？                   当窗口大小小于k时候扩大窗口
    2、什么时候应该缩小窗口？                   当窗口大小大于k时候缩小窗口
    3、什么时候得到一个合法的答案？              当窗口大小等于k时候，判断是否存在重复元素
"""


def containsNearbyDuplicate(nums, k):
    """
    :param nums:
    :param k:
    :return:
    """
    left = right = 0
    window = set()
    while right < len(nums):
        c = nums[right]
        if c in window:
            return True
        window.add(c)
        right += 1
        while right - left > k:
            d = nums[left]
            window.remove(d)
            left += 1
    return False