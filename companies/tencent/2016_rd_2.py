# -*- coding:utf-8 -*-
 
"""ACCEPT"""

class Gift:
    def getValue(self, gifts, n):
        # write code here
        sorted_gifts = sorted(gifts, key=lambda t: gifts.count(t), reverse=True)
        if sorted_gifts.count(sorted_gifts[0]) * 2 > n:
            return sorted_gifts[0]
        else:
            return 0