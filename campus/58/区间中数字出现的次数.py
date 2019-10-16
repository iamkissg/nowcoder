import sys


class Solution:

    def count_X(self, N, M, X):
        num_gen = (str(i) for i in range(N, M+1))
        count = 0
        for a in num_gen:
            count += a.count(X)

        return count


if __name__ == "__main__":
    sol = Solution()

    N, M, X = list(map(int, input().split()))
    X = str(X)
    # print(N, M, X)
    print(sol.count_X(N, M, X))
    