# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        elif number > 2:
            a, b = 1, 2
            for _ in range(2, number):
                a, b = b, a+b
            return b