# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        elif number > 2:
            a, b = 1, 2
            for _ in range(2, number):
                a, b = b, a+b
            return b

if __name__ == "__main__":
    sol = Solution()
    print(sol.jumpFloor(3))