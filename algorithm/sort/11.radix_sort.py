"""
基数排序
    多关键字排序：假如有一个员工表，要求按照薪资排序，年龄相同的员工按照年龄排序
        先按照年龄进行排序，再按照薪资进行稳定的排序
    对32，13，94，52，17，54， 93排序，是否可以看作是多关键字排序

    时间复杂度O(kn)
    空间复杂度O(k + n)
    k 表示数字位数 (k -> log10n) 和数的范围有关

    ！！！ 与快速排序的比较 O（nlogn） -> (log2n)

    字符串如何排序？？？？
    同样也是第一位比，第二位比。。。。。
    abcd
    ab00

"""

import random


def radix_sort(li):
    max_num = max(li)
    # 数有几位则排序几次
    it = 0
    while 10 ** it <= max_num:
        # 按照每一位进行分桶，分10个桶
        buckets = [[] for _ in range(10)]
        # 将val的各位进行分桶
        for val in li:
            digit = (val // 10 ** it) % 10
            buckets[digit].append(val)

        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1


if __name__ == '__main__':
    l1 = [random.randint(0, 1000) for _ in range(10000)]
    random.shuffle(l1)
    radix_sort(l1)
    print(l1)
