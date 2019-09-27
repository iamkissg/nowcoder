import sys

row_opts = [-1, 1, 0, 0]
col_opts = [0, 0, -1, 1]

'''
事后完成的, 样例通过了, 估计没错
'''

class Solution:

    def __init__(self):
        self.end = '#'
    
    def game_over(self, mat):
        for row in range(1, len(mat)-1):
            for col in range(1, len(mat[0])-1):
                if mat[row][col] == self.end:
                    continue
                val = mat[row][col]
                for i in range(4):
                    if mat[row+row_opts[i]][col+col_opts[i]] == val:
                        return False
        else:
            return True

    def walk_around(self, mat, row, col, visited):
        if mat[row][col] == self.end:
            return []
        elif mat[row+row_opts[0]][col+col_opts[0]] != mat[row][col] and \
                mat[row+row_opts[1]][col+col_opts[1]] != mat[row][col] and \
                mat[row+row_opts[2]][col+col_opts[2]] != mat[row][col] and \
                mat[row+row_opts[3]][col+col_opts[3]] != mat[row][col]:
            return [(row, col)]
        else:
            result = {(row, col)}
            visited.add((row, col))
            for i in range(4):
                if (row+row_opts[i], col+col_opts[i]) in visited:
                    continue
                if mat[row+row_opts[i]][col+col_opts[i]] == mat[row][col]:
                    result.update(self.walk_around(mat, row+row_opts[i], col+col_opts[i], visited))
            return result

    def remove_empty_column(self, mat):
        for col in range(1, len(mat[0])-1):
            if all([mat[row][col] == self.end for row in range(1, len(mat)-1)]) and \
                    not all([mat[row][col+1] == self.end for row in range(1, len(mat)-1)]):

                for row in range(1, len(mat)-1):
                    mat[row][col], mat[row][col+1] = mat[row][col+1], mat[row][col]
        return mat

    def up_down(self, mat):
        for col in range(1, len(mat[0])-1):
            if not all([mat[row][col] == self.end for row in range(1, len(mat)-1)]):
                for row in range(len(mat)-2, 0, -1):
                    if mat[row][col] == self.end:
                        for to_swap_row in range(row-1, 0, -1):
                            if mat[to_swap_row][col] == self.end:
                                continue
                            mat[row][col], mat[to_swap_row][col] = mat[to_swap_row][col], mat[row][col]
        return mat



    def play(self, mat):
        
        while not self.game_over(mat):

            d = {}
            for row in range(1, len(mat)-1):
                for col in range(1, len(mat[0])-1):
                    if mat[row][col] == self.end:
                        continue
                    val = mat[row][col]
                    if val not in d:
                        d[val] = set()
                    d[val].add(frozenset(self.walk_around(mat, row, col, set())))
            d = [(v, k) for k, vs in d.items() for v in vs]
            sd = sorted(d,
                key=lambda t: (len(t[0]), -int(t[1]), min([row for row, col in t[0]]), min([col for row, col in t[0]])),
                reverse=True)

            for row, col in sd[0][0]:
                mat[row][col] = '#'
            mat = self.remove_empty_column(mat)
            mat = self.up_down(mat)

        result = 0
        for row in range(1, len(mat)-1):
            for col in range(1, len(mat[0])-1):
                if mat[row][col] != self.end:
                    result += 1
        return result
                

if __name__ == "__main__":
    sol = Solution()

    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        M, N = map(int, sys.stdin.readline().strip().split())
        mat = [sys.stdin.readline().strip() for _ in range(M)]
        mat = [['#']*(N+2)] + [['#']+list(row)+['#'] for row in mat] + [['#']*(N+2)]
        print(sol.play(mat))


'''
4
5 5
25254
32234
23222
22222
22443
4 5
11334
42455
02340
14222
3 3
010
001
110
4 4
0322
0310
1210
3220
'''

'''
6
4 4
0322
0310
1210
3220
4 4
032#
031#
121#
3222
4 4
0###
0#2#
131#
331#
4 4
####
02##
01##
11##
4 4
####
####
0###
02##
4 4
####
####
####
2###
'''

'''
1
4 4
####
0#2#
0#1#
1#1#
'''