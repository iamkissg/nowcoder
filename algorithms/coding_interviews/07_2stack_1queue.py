# -*- coding:utf-8 -*-

"""ACCEPT"""


class Solution:
    def __init__(self):
        self.a = []
        self.b = []
    
    def push(self, node):
        # write code here
        self.a.append(node)
        
    def pop(self):
        # return xx
        if len(self.a) == 0:
            raise RuntimeError()
            
        for i in range(len(self.a)-1):
            self.b.append(self.a.pop())
        result = self.a.pop()
        for i in range(len(self.b)):
            self.a.append(self.b.pop())
        
        return result