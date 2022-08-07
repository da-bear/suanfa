# 协程（Coroutine），也可以被称为微线程，是一种用户态内的上下文切换技术。简而言之，其实就是通过一个线程实现代码块相互切换执行
def func1():
    print(1)
    ...
    print(2)


def func2():
    print(3)
    ...
    print(4)


if __name__ == '__main__':
    # 在Python中有多种方式可以实现协程，例如：
    #
    # greenlet，是一个第三方模块，用于实现协程代码（Gevent协程就是基于greenlet实现）
    # yield，生成器，借助生成器的特点也可以实现协程代码。
    # asyncio，在Python3.4 中引入的模块用于编写协程代码。
    # async & await，在Python3.5 中引入的两个关键字，结合asyncio模块可以更方便的编写协程代码。
    func1()
    func2()
