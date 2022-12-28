"""
题目：
    给定一个数组 nums，编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。
    请注意，必须在不复制数组的情况下原地对数组进行操作。
"""


def moveZeroes(nums):
    slow, fast = 0, 0
    for _ in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    for i in range(slow, len(nums)):
        nums[i] = 0
