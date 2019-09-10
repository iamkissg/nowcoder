# -*- coding:utf-8 -*-

# 数学归纳法
# 1: 1
# 2: 2
# 3: 1 + 2 + 1
# 4: 1 + 1 + 1 + 2 + 3


class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.jumpFloorII(3))