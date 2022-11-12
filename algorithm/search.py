"""
列表查找
    线性查找： 复杂度O(n)
            内置函数index（）使用的是线性查找，因为二分查找需要的是排序好的数组
    二分查找:  复杂度O(logn)
"""
from cal_time import timeit


@timeit
def linear_search(li, val):
    for index, v in enumerate(li):
        if v == val:
            return index
    else:
        return None


@timeit
def binary_search(li, val):
    if len(li) == 0:
        return None
    left = 0
    right = len(li) - 1
    while left <= right:  # 后选区有值
        mid = (left + right) // 2
        if li[mid] > val:  # 待查找的值在mid的左侧
            right = mid - 1
        elif li[mid] < val:  # 待查找的值在mid的右侧
            left = mid + 1
        else:
            return mid
    else:
        return None


if __name__ == '__main__':
    # l1 = [1, 2, 3, 4, 5, 6, 7, 8]
    l1 = list(range(10000000))
    print(linear_search(l1, 999999))
    print(binary_search(l1, 999999))
