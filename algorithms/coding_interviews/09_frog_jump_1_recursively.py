# -*- coding:utf-8 -*-


"""运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        elif number > 2:
            return self.jumpFloor(number-1)+self.jumpFloor(number-2)

if __name__ == "__main__":
    sol = Solution()
    print(sol.jumpFloor(10))