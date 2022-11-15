"""
如何实现一个队列
    队列可以用列表实现吗？
        出队：删除该元素 remove， pop 删除一个元素会使得元素往前挪动 O(n)
             对首index + ， 队尾始终保持最后一个 （数组无法进队）
             若用python list即使 可以append
             最后占用大量内存，有用的又少

        队列不可用🚫列表实现


    环形队列的实现  -> 环形队列

        ！！！ 当队首的指针 rear == MaxSize  +  1 时，再前进一个位置就自动到0
        实现方式：求余数运算
        队首指针前进1: front = (front + 1) % MaxSize
        队尾指针前进1：rear = (rear + 1) % MaxSize
        队空条件：rear == front
        队满条件：(rear + 1) % MaxSize == front
"""
from collections import deque


class Queue:

    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.front = 0  # 队首的指针
        self.rear = 0  # 队尾指针
        self.size = size

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        """
        判断队空
        """
        return self.rear == self.front

    def is_filled(self):
        """
        判断队满
        """
        return (self.rear + 1) % self.size == self.front



if __name__ == '__main__':
    # q = Queue(6)
    # for i in range(5):
    #     q.push(i)
    # print(q.pop())
    # q.push(7)

    # q = deque()
    # q.append(1)  # 队尾进队
    # q.append(2)
    # q.append(3)
    # print(q.popleft())  # 队首出队

    def tail_tt(n):
        with open('test', 'r') as f:
            q = deque(f, n)
            return q


    for line in tail_tt(5):
        print(line, end='')
