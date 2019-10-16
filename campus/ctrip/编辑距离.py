#!/usr/bin/env python  
# coding=utf-8  

import sys

class Solution:

    def edit_distance(self, s1, s2):
        n1, n2 = len(s1), len(s2)

        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(n1+1):
            dp[i][0] = i
        for j in range(n2+1):
            dp[0][j] = j
        
        for i, c1 in enumerate(s1, start=1):
            for j, c2 in enumerate(s2, start=1):
                if c1 == c2:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[n1][n2]


sol = Solution()
while 1:
    s1, s2 = input().split('<ctrip>')
    print(sol.edit_distance(s1, s2))
