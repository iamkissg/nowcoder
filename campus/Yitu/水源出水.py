import sys

def draw(mat, a, b, c):
    if c == 0:
        return
    
    # if mat[a][b] < c:
    #     mat[a][b] = c
    # mat[a][b] = c
    # for i in range(1, c):
    #     if a-i >= 0:
    #         mat[a-i][b] = c-i
    #         # draw(mat, a-i, b, c-i)
    #     if a+i < len(mat):
    #         # draw(mat, a+i, b, c-i)
    #         mat[a+i][b] = c-i
    #     if b-i >= 0:
    #         # draw(mat, a, b-i, c-i)
    #         mat[a][b-i] = c-i
    #     if b+i < len(mat[0]):
    #         # draw(mat, a, b+i, c-i)
    #         mat[a][b+i] = c-i
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if abs(a-i) >= c-1:
                continue
            elif abs(b-j) >= c-1:
                continue
            mat[i][j] = min([c-abs(a-i), c-abs(b-j)])
        
if __name__ == "__main__":


    T = int(input())
    i = 1
    for i in range(T):
        n, m, a, b, c = map(int, sys.stdin.readline().strip().split())
        mat = [[0 for col in range(m)] for row in range(n)]
        draw(mat, a, b, c)
        print('Case #{}:'.format(i+1))
        for row in mat:
            print(' '.join(map(str, row)))
