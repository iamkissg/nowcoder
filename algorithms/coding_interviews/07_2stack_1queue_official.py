# -*- coding:utf-8 -*-

"""ACCEPT"""


class Solution:
    def __init__(self):
        self.a = []
        self.b = []
    
    def push(self, node):
        # write code here
        # a 用于接收新的输入
        self.a.append(node)
        print(self.a)
        
    def pop(self):
        # pop 的时候要 pop 队列头的元素
        # 当 b 为空时, 将 a 栈的元素都 pop 都 b 中, 此时, b 的栈顶就是原 a 的栈底, 即最早入"队"的元素
        # 所以当 b 不为空时, 尽管从 b pop 即可, 否则, 将 a 栈的元素全部 pop 到 b 中.
        if not self.a and not self.b:
            raise ValueError('Pop from empty queue')
        if not self.b:
            for _ in range(len(self.a)):
                self.b.append(self.a.pop())
        result = self.b.pop()
        print(self.a, self.b)
        return result

if __name__ == "__main__":
    sol = Solution()
    sol.push(1)
    sol.push(2)
    sol.push(3)
    sol.pop()
    sol.pop()
    sol.push(4)
    sol.pop()
    sol.push(5)
    sol.pop()
    sol.pop()