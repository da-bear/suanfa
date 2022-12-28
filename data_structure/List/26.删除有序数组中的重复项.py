"""
题目：
    给你一个升序排列的数组nums，请你原地删除重复出现的元素，使每个元素只出现一次，返回删除后数组的新长度。元素的相对顺序应该保持 一致

分析：
    原地删除，不允许new新数组，只能在原数组上操作，然后返回一个长度，这样就可以通过返回的长度和原始数组得到我们去重后的元素有哪些了
    由于数组已经排序，所以重复的元素一定连在一起，找出它们并不难。但如果毎找到一个重复元素就立即原地删除它，
    由于数组中删除元素涉及数据搬移，整个时间复杂度是会达到 O(N^2)。

    高效解决这道题就要用到快慢指针技巧：
        我们让慢指针slow走在后面，快指针fast走在前面探路，找到一个不重复的元素就赋值给slow并让slow前进一步。

         1 2 2 3 5 5 6 6 6 8 7
         1 2 3 5 6 8 7 6 6 8 7
                     s
                             f
"""


def removeDuplicates(nums):
    """
    :param nums: target list
    :return: after list length
    """
    if len(nums) == 0:
        return 0
    slow, fast = 0, 0
    for _ in range(len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1

    return slow + 1







