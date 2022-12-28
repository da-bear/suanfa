"""
题目：
    给你一个数组 nums 和一个值 val，你需要原地移除所有数值等于val的元素，并返回移除后数组的新长度。
分析：
    题目要求我们把 nums 中所有值为 val 的元素原地删除，依然需要使用快慢指针技巧：
    如果 fast 遇到值为 val 的元素，则直接跳过，否则就赋值给 slow 指针，并让 slow 前进一步。
    这和前面说到的数组去重问题解法思路是完全一样的

注意：
    这里和有序数组去重的解法有一个细节差异，我们这里是先给 nums[slow] 赋值然后再给 slow+=1，
    这样可以保证 nums[0..slow-1] 是不包含值为 val 的元素的，最后的结果数组长度就是 slow。
"""


def removeElement(nums, val):
    if len(nums) == 0:
        return 0
    slow, fast = 0, 0
    for _ in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow
