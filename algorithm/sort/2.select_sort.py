"""
选择排序
    选出最小的与无序区第一个进行交换
    趟、 有序区、无序区
    O(n2)
"""


def select_sort_simple(li):
    """
    理解思路
    """
    li_new = []  # 开辟新的内存
    for i in range(len(li)):
        min_val = min(li)  # 时间复杂度为O(n)
        li_new.append(min_val)
        li.remove(min_val)  # 删除的时间复杂度O(n)
    return li_new


def select_sort(li):
    """
    有效的方法
    """
    for i in range(len(li) - 1):  # 同样是n-1趟
        min_index = i  # 默认最开始无序区第一个值最小
        for j in range(i, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        if min_index != i:
            li[i], li[min_index] = li[min_index], li[i]


if __name__ == '__main__':
    l1 = [3, 4, 5, 7, 1, 3, 2, 9]
    # print(select_sort_simple(l1))
    select_sort(l1)
    print(l1)
