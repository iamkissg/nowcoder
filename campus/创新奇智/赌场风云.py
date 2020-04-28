import sys


class Solution:
    def win_probability(self, m, p, x):
        if p == 0:
            return 0.
        else:
        # elif p >= 0.5:
            wp = 1.0
            for _ in range(m):
                x *= 2
                wp *= p
                if x >= 1000000:
                    return wp
            return 0.
        # else:
        #     wp = 1.0
        #     for _ in range(m):
        #         x = 1.5 * x
        #         wp *= p
        #         if x >= 1000000:
        #             return wp
        #     return 0.



if __name__ == "__main__":
    sol = Solution()
    m, p, x = list(map(float, input().split()))
    m = int(m)
    print('%.4f' % sol.win_probability(m, p, x))