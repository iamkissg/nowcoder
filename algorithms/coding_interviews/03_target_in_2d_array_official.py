# -*- coding:utf-8 -*-

"""ACCEPT"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # Empty array
        if not array[0]:
            return False
        
        # Non-empty array
        rows = len(array)
        cols = len(array[0])
        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            if array[row][col] > target:
                col -= 1
            elif array[row][col] < target:
                row += 1
            else:
                return True
        else:
            return False