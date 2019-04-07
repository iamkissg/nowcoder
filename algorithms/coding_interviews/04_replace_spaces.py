# -*- coding:utf-8 -*-

"""ACCEPT"""

class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        ns = s.replace(' ', '%20')
        return ns