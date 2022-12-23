"""
约数：如果整数a能被整数b整除，那么a叫做b的倍数，b叫做a的约数
给定两个整数a， b 两个数的所有公共约数中的最大值叫做最大公约数
eg： 12 和 16的最大公约数是4

如何计算两个最大公约数
    辗转相除法
        gcd(a,b) = gcd(b, a mod b)
    更相减损术

应用：
    利用欧几里得算法实现一个分数类，支持分数的四则运算
"""


def gcd_1(a, b):
    if b == 0:
        return a
    else:
        return gcd_1(b, a % b)


class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    @staticmethod
    def gcd(a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def zgs(self, a, b):
        x = self.gcd(a, b)
        return a * b / x

    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fm = self.zgs(a, b)
        fz = a * fm / b + c * fm / d
        return Fraction(fz, fm)

    def __str__(self):
        return "%d/%d" % (self.a, self.b)


if __name__ == '__main__':
    f1 = Fraction(1, 3)
    f2 = Fraction(1, 2)
    print(f1 + f2)
