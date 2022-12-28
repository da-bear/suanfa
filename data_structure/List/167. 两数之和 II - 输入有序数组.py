"""
题目：
    给你一个下标从1开始的整数数组numbers，该数组已按非递减顺序排列，
    请你从数组中找出满足相加之和等于目标数 target 的两个数。
    如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

分析：
    todo: 只要数组有序，就应该想到双指针技巧。这道题的解法有点类似二分查找，通过调节left和right就可以调整sum的大小
"""


def twoSum(numbers, target):
    """
    :param numbers: 整数数组
    :param target: 目标数
    :return: numbers[index1], numbers[index2]
    """
    left = 0
    right = len(numbers) - 1

    while left <= right:
        s = numbers[left] + numbers[right]
        if s == target:
            # 题目要求下标从1开始
            return [left+1, right+1]
        elif s > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]

