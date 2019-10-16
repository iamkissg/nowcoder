import sys


class Solution:

    def go_home(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a+b
        return b

if __name__ == "__main__":
    sol = Solution()

    distance = int(input())
    print(sol.go_home(distance))
    