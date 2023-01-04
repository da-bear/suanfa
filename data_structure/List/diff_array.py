"""
差分数组类
"""


class Difference(object):

    def __init__(self, nums):
        self.diff = self.diffList(nums)

    @staticmethod
    def diffList(nums):
        """
        构造差分数组
        """
        diff = [0 for _ in range(len(nums))]
        diff[0] = nums[0]
        for i in range(1, len(nums)):
            diff[i] = nums[i] - nums[i - 1]
        return diff

    def result(self):
        """
        获取操作后的数组
        """
        res = []
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]
        return res

    def increment(self, i, j, inc):
        """
        对数组某一个区间的数进行增减（包含边界值）
        """
        self.diff[i] += inc
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= inc
