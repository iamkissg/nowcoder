# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 1, 1
            for i in range(1, n-1):
                a, b = b, a+b
            return b