# -*- coding:utf-8 -*-


# from math import isclose


def isclose(a, b, eps=1e-8):
    if abs(a-b) < eps:
        return True
    else:
        return False

class Solution:
    def Power(self, base, exponent):
        # write code here

        def unsigned_power(base, exponent):
            result = 1.0
            for _ in range(exponent):
                result *= base
            return result


        if isclose(base, 0) and exponent < 0:
            return 0.0

        abs_exponent = abs(exponent)

        result = unsigned_power(base, abs_exponent)
        if exponent < 0:
            result = 1.0 / result
        return result


if __name__ == "__main__":
    sol = Solution()

    print(sol.Power(2, 2))
    print(sol.Power(2, -2))
    print(sol.Power(2, 0))
    print(sol.Power(0, 2))
    print(sol.Power(0, -1))
    print(sol.Power(-1, 2))
    print(sol.Power(-1, 0))
    print(sol.Power(-2, 3))