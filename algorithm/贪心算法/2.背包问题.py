"""
一个小偷在某个商店发现有n个商品，第i个商品价值V元，重w千克。他希望拿走的价值尽量高，但他的背包最多只能容纳W千克的东西。他应该拿走哪些
商品？
    0-1背包：对于一个商品，小偷要么把它完整拿走，要么留下。不能只拿走一部分，或把一个商品拿走多次。（商品为金条）
    分数背包：对于一个商品，小偷可以拿走其中任意一部分。（商品为金砂）

举例：
    商品1：V=6O W=10
    商品2：VD=100 W2=20
    商品3： Vg=120 Wg=30
    背句容量：W=50

对于0-1背包和分数背包，贪心算法是否都能得到最优解？为什么
"""

goods = [(60, 10), (100, 20), (120, 30)]
goods.sort(key=lambda x: x[0] / x[1], reverse=True)


def fractional_package(target, w):
    """
    target: goods
    w: 背包剩余重量
    """
    m = [0 for _ in range(len(target))]
    total_val = 0
    for i, (prize, weight) in enumerate(target):
        if w >= weight:
            m[i] = 1
            total_val += prize
            w -= weight
        else:
            m[i] = w / weight
            total_val += m[i] * prize
            break

    return m, total_val


print(fractional_package(goods, 50))
