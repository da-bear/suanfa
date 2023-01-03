"""
题目；
    给定一个整数数组nums，处理以下类型的多个查询
    计算索引left和right（包含left和right）之间的nums元素的和，其中left <= right

    实现 NumArray 类：
        NumArray(int[] nums) 使用数组 nums 初始化对象
        int sumRange(int i, int j) 返回数组nums中索引left和right之间的元素的总和，
             包含left和right两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] )

    new 一个新的数组 preSum 出来，preSum[i] 记录 nums[0..i-1] 的累加和
"""


class NumArray:

    def __init__(self, nums):
        self.nums = self.init_nums(nums)

    @staticmethod
    def init_nums(nums):
        tmp = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(tmp)):
            tmp[i] = tmp[i - 1] + nums[i - 1]

        return tmp

    def sumRange(self, left, right):
        return self.nums[right + 1] - self.nums[left]


if __name__ == '__main__':
    a = NumArray([-2, 0, 3, -5, 2, -1])
    a.sumRange(0, 2)
