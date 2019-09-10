# -*- coding:utf-8 -*-


# 运行时间：23ms
# 占用内存：5864k

# 该问题可以看作是斐波那契问题的变种.
# n 级台阶, 可以看作是1. 先跳一级, 后续的 n-1 级台阶按照 f(n-1) 算;
#                  2. 先跳两级, 后续的 n-2 级台阶按照 f(n-2) 算
# 所以 f(n) = f(n-1) + f(n-2)


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
    print(sol.jumpFloor(10))