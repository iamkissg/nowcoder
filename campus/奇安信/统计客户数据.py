import sys


class Solution:

    def func(self, arr, mat):
        n = len(mat)
        res = []

        for l, r, k in mat:
            res.append(arr[l-1: r].count(k))
        
        return res


if __name__ == "__main__":
    sol = Solution()

    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    mat = [list(map(int, input().split())) for _ in range(q)]

    # print('Input')
    # print(n)
    # print(arr)
    # print(q)
    # for row in mat:
    #     print(row)
    res = sol.func(arr, mat)
    for r in res:
        print(r)