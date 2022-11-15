"""
桶排序
    在计数排序中，如果元素的范围比较大（1- 1亿），如何改造算法
    桶排序（Bucket Sort): 首先将元素分在不同的桶中，在对每个桶中的元素排序
"""
import random


def bucket_sort(li, n=100, max_num=10000):
    """
    :param li: 待排序的列表
    :param n: 需要建的桶的数
    :param max_num: 列表中最大数
    :return:
    """
    # 建桶
    buckets = [[] for _ in range(n)]
    for val in li:
        # 当前数进哪个桶， 桶号（0-99）
        # max_num // n 每个桶中放多少个数 （注意！！！！ 桶号从0开始）
        i = min(val // (max_num // n), n - 1)  # 表示var放到第几号桶里
        buckets[i].append(val)
        # 每防置一个数，需要将桶里的数进行排序，类似于冒泡的方式，将数进行排序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    # 将桶中的数取出
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)

    return sorted_li


if __name__ == '__main__':
    l1 = [random.randint(0, 10000) for _ in range(1000)]
    random.shuffle(l1)
    # print(l1)
    print(bucket_sort(l1))