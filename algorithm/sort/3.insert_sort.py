"""
插入排序
    列表中的数，比作手里的牌， 需要将手里的牌进行排序，从手里的第二张牌摸出来，再插回去
        初始时手里（有序区）只有一张牌
        每次（从无序区摸一张牌，插入到手里以有牌的正确位置）
    要点：手里的牌，摸到的牌
    时间复杂度O(n2)
"""


def insert_sort(li):
    for i in range(1, len(li)):  # 要摸出重新进行插回的牌
        tmp = li[i]  # 摸出的这张牌，要将摸出的牌和手里的牌进行比较
        j = i - 1  # 手里的牌在列表中的index
        while j >= 0 and li[j] > tmp:  # 手里至少会有一张牌，手里的牌比摸到的牌大，需要移动
            li[j + 1] = li[j]  # 往后移动
            j -= 1  # 手里的第一张牌的指针
        li[j + 1] = tmp


if __name__ == '__main__':
    l1 = [3, 1, 2, 5, 9, 8, 4, 7, 6]
    print("before sort:", l1)
    insert_sort(l1)
    print("after sort:", l1)
