"""
题目:
    给你一个整数数组 nums 和一个整数 k，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目

    输入：nums = [10,5,2,6], k = 100
    输出：8
    解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
    需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。

    输入：nums = [1,2,3], k = 0
    输出：0

分析:
    维护一个窗口在 nums 上滑动，然后计算那些元素之积小于 k 的窗口个数即可。
    1、什么时候应该扩大窗口？ --- > 当窗口内元素之积小于k
    2、什么时候应该缩小窗口？ --- > 当窗口内元素之积大于k
    3、什么时候得到一个合法的答案？ --- > 窗口内元素的所有子数组都是合法子数组
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


if __name__ == '__main__':
    a = [10, 5, 2, 6]
    numSubarrayProductLessThanK(a, 100)


