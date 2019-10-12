import sys
class Solution:
    def __init__(self):
        a, b = 3, 3
        self.fib = [a, b]
        for _ in range(2, 37):
            a, b = b, a+b
            self.fib.append(b)

    def max_height(self, n_day):
        height = 0
        for d in range(n_day-1, -1, -1):
            height = (height + self.fib[d]) * 2
        return height


if __name__ == "__main__":
    sol = Solution()


    for line in sys.stdin:
        n_day = int(line)
        print(sol.max_height(n_day))