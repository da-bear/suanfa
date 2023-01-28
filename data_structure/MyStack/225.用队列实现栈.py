"""
题目：
    请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（push、top、pop 和 empty）。

    实现 MyStack 类：
    void push(int x) 将元素 x 压入栈顶。
    int pop() 移除并返回栈顶元素。
    int top() 返回栈顶元素。
    boolean empty() 如果栈是空的，返回 true ；否则，返回 false

注意：
    你只能使用队列的基本操作 —— 也就是 push to back、peek/pop from front、size 和 is empty 这些操作。
    你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。

示例：
    输入：["MyStack", "push", "push", "top", "pop", "empty"]
    [[], [1], [2], [], [], []]
    输出：
    [null, null, null, 2, 2, false]

    解释：
    MyStack myStack = new MyStack();
    myStack.push(1);
    myStack.push(2);
    myStack.top(); // 返回 2
    myStack.pop(); // 返回 2
    myStack.empty(); // 返回 False

分析：
    两个队列q1，q2，--- q1 用于存储栈内元素，q2作为入栈操作的辅助队列
    入栈操作：首先将元素入对q2，将q1的全部元素依次出队并入对到q2，
    此时q2的前端元素即为新入栈的元素

"""

from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    # 添加元素到栈顶
    def push(self, x: int) -> None:
        # x 是队列的队尾，是栈的栈顶
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    # 删除栈顶元素并返回
    def pop(self):
        return self.q1.popleft()

    # 返回栈顶元素
    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1
