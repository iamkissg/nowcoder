# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        return 2**(number-1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.jumpFloor(3))