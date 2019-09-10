# -*- coding:utf-8 -*-
class Solution:

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return None

        start = 0

        n_rows = len(matrix)
        n_cols = len(matrix[0])

        result = []
        while n_cols > start * 2 and n_rows > start * 2:
            result += self.printCircle(matrix, n_cols, n_rows, start)
            start += 1
        return result


    def printCircle(self, matrix, n_cols, n_rows, start):
        end_col = n_cols - start - 1  # right most column index
        end_row = n_rows - start - 1  # bottom most row index

        result = []
        for i in range(start, end_col+1):
            # print(matrix[start][i])
            result.append(matrix[start][i])

        if start < end_row:
            for i in range(start+1, end_row+1):
                # print(matrix[i][end_col])
                result.append(matrix[i][end_col])

        if start < end_col and start < end_row:
            for i in reversed(range(start, end_col)):
                # print(matrix[end_row][i])
                result.append(matrix[end_row][i])

        if start < end_col and start < end_row - 1:
            for i in reversed(range(start+1, end_row)):
                # print(matrix[i][start])
                result.append(matrix[i][start])

        return result

if __name__ == "__main__":
    m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10,11, 12], [13, 14, 15, 16]]

    sol = Solution()
    print(sol.printMatrix(m))