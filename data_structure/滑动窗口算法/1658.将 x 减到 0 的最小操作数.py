"""
题目:
    给你一个整数数组nums和一个整数x。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从x中减去该元素的值。
    请注意，需要修改数组以供接下来的操作使用, 如果可以将x恰好减到0，返回最小操作数；否则，返回 -1

    输入：nums = [1,1,4,2,3], x = 5
    输出：2
    解释：最佳解决方案是移除后两个元素，将 x 减到 0。

    输入：nums = [5,6,7,8,9], x = 4
    输出：-1

分析:
    等价于让你寻找 nums 中元素和为 sum(nums) - x 的最长子数组
        有： 返回 len(mums) - len(nums[left : right])
        无： 返回-1

    target = sum(nums) - x
    1、什么时候应该扩大窗口？ --- > 当窗口内元素之和小于target
    2、什么时候应该缩小窗口？ --- > 当窗口内元素之和小于target
    3、什么时候得到一个合法的答案？ --- > 当窗口内元素之和等于target时，找到一个符合条件的子数组，我们想找的是最长的子数组长度
"""


def minOperations(nums, x):
    left = right = 0
    # 计算target
    target = sum(nums) - x
    # 窗口内的元素和
    windowSum = 0
    # 子数组的最大长度
    maxLen = -1

    while right < len(nums):
        # 扩大窗口
        windowSum += nums[right]
        right += 1
        while windowSum > target and left < right:  # 控制边界
            # 缩小窗口
            windowSum -= nums[left]
            left += 1

        if windowSum == target:
            maxLen = max(maxLen, right - left)

    return len(nums) - maxLen if maxLen >= 0 else -1


if __name__ == '__main__':
    num = [8828, 9581, 49, 9818, 9974, 9869, 9991, 10000, 10000, 10000, 9999, 9993, 9904, 8819, 1231, 6309]
    print(minOperations(num, 134365))




