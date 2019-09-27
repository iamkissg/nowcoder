import sys


class Solution:

    def step_to_n(self, n):
        n = abs(n)

        step = 0
        total = 0
        while True:
            step += 1
            total += step

            positions = {i for i in  range(total, 0, -2)}
            if n in positions:
                return step


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    sol = Solution()
    print(sol.step_to_n(n))