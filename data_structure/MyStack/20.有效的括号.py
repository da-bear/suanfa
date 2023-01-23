"""
题目：
    给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

    有效字符串需满足：
        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        每个右括号都有一个对应的相同类型的左括号。


    输入：s = "()"
    输出：true
"""


def isValid(s):
    match = {'}': '{', ']': '[', ')': '('}
    stk = []
    for ch in s:
        if ch in ['{', '[', '(']:
            stk.append(ch)
        else:
            if len(stk) == 0:
                return False
            elif stk[-1] == match[ch]:
                stk.pop()
            else:
                return False
    if len(stk) == 0:
        return True
    else:
        return False
