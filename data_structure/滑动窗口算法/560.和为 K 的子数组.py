# """
# 题目:
#     给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数
#
#     输入：nums = [1,1,1], k = 2
#     输出：2
#     输入：nums = [1,2,3], k = 3
#     输出：2
# """
#
#
# def subarraySum(nums, k):
#     left = right = 0
#     windowSum = 0
#     cnt = 0
#     while right < len(nums):
#         windowSum += nums[right]
#         right += 1
#
#         while windowSum != k and left < right:
#             windowSum -= nums[left]
#             left += 1
#
#         if windowSum == k:
#             cnt += 1
#
#     return cnt
#
#
# if __name__ == '__main__':
#     a = [-1, -1, 1]
#     print(subarraySum(a, 0))
