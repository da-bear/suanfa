"""
题目：
    给你一个整数数组 nums 和两个整数 k 和 t。
    请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
    如果存在则返回 true，不存在返回 false

    输入：nums = [1,2,3,1], k = 3, t = 0
    输出：true

    输入：nums = [1,0,1,1], k = 1, t = 2
    输出：true

    输入：nums = [1,5,9,1,5,9], k = 2, t = 3
    输出：false

    0 <= nums.length <= 2 * 104
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 104
    0 <= t <= 231 - 1

分析：
    1、什么时候应该扩大窗口？  当窗口大小小于等于 k 时，扩大窗口，包含更多元素。
    2、什么时候应该缩小窗口？  当窗口大小大于 k 时，缩小窗口，减少窗口元素。
    3、什么时候得到一个合法的答案？  窗口大小小于等于 k，且窗口中存在两个不同元素之差小于 t 时，找到一个答案。
        那么我如何在窗口 [left, right) 中快速判断是否有元素之差小于 t 的两个元素呢？
            这就需要使用到TreeSet 利用二叉搜索树结构寻找「地板元素」和「天花板元素」的特性了
            后面的课程 动手实现 TreeMap/TreeSet 中详细讲解了 TreeSet 的底层原理，这里你只要知道 TreeSet 如何和滑动窗口算法结合即可
"""


def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    """
    :param nums:
    :param indexDiff:
    :param valueDiff:
    :return:
    """
    pass
