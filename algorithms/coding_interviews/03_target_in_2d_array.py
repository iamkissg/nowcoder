# -*- coding:utf-8 -*-

"""ACCEPT"""

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if not array[0]:
            return False
        if target < array[0][0] or target > array[-1][-1]:
            return False
        else:
            for i in range(len(array)):
                if target in array[i]:
                    return True
            else:
                return False