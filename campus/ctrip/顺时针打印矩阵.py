#!/usr/bin/env python  
# coding=utf-8

class Solution:

    # matrix类型为二维列表，需要返回列表
    def print_matrix(self, mat):
        if not mat:
            return []

        start = 0
        n_row, n_col = len(mat), len(mat[0])

        res = []
        while n_row > start * 2 and n_col > start * 2:
            res += self.print_circle(mat, n_col, n_row, start)
            start += 1
        return res

    def print_circle(self, mat, n_col, n_row, start):
        end_col = n_col - start - 1  # right most column index
        end_row = n_row - start - 1  # bottom most row index

        res = []
        for i in range(start, end_col+1):
            # print(mat[start][i])
            res.append(mat[start][i])

        for i in range(start+1, end_row+1):
            # print(mat[i][end_col])
            res.append(mat[i][end_col])

        # 特殊处理高瘦型和矮胖型矩阵
        if start < end_row:
            for i in range(end_col-1, start-1, -1):
                # print(mat[end_row][i])
                res.append(mat[end_row][i])

        if start < end_col:
            for i in range(end_row-1, start, -1):
                # print(mat[i][start])
                res.append(mat[i][start])

        return res


sol = Solution()
while 1:
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    res = sol.print_matrix(mat)

    print(','.join(map(str, res)))