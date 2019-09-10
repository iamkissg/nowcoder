# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here

        def is_odd(n):
            return n & 1

        condition = is_odd

        odds = []
        evens = []
        for i, n in enumerate(array):
            if condition(n):
                odds.append(n)
            else:
                evens.append(n)
        return odds + evens


if __name__ == "__main__":
    sol = Solution()

    print(sol.reOrderArray([1, 2, 343, 3, 312, 5]))