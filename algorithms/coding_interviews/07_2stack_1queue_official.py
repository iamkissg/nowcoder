# -*- coding:utf-8 -*-

"""ACCEPT"""


class Solution:
    def __init__(self):
        self.a = []
        self.b = []
    
    def push(self, node):
        # write code here
        self.a.append(node)
        print(self.a)
        
    def pop(self):
        # return xx
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