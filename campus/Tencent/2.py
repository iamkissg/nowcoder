#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。

# 20% 


from itertools import combinations

class Solution:
    def __init__(self):
        self.memo = {}

    def is_covered(self, x, y):
        p1, p2 = abs(x), abs(y)
        q1, q2 = abs(x-y), abs(x+y)
        
        if p1 > p2:
            p1, p2 = p2, q1
        if q1 > q2:
            q1, q2 = q2, q1
        if (p1, p2, q1, q2) in self.memo:
            return self.memo[(p1, p2, q1, q2)]
        else:
            self.memo[(p1, p2, q1, q2)] = p1 >= q1 and p2 <= q2
        return self.memo[(p1, p2, q1, q2)]

    # a = (p1, p2) if p1 < p2 else (p2, p1)
    # b = (q1, q2) if q1 < q2 else (q2, q1)
    # # print(a, b)

    # return a[0] >= b[0] and a[1] <= b[1]
    

    def play_game(self, arr):
        # result = 0
        # for x, y in combinations(arr, 2):
        # # for i 
        #     # print(x, y, is_covered(x, y))
        #     result += 1 if is_covered(x, y) else 0
        # return result

        # return len([1 for x, y in zip(arr[:-1], arr[1:]) if is_covered(x,y)])
        return len([1 for x, y in combinations(arr, 2) if self.is_covered(x, y)])
        # lena = len(arr)
        # return len([1 for i in range(lena-1) for j in range(i+1, lena) if is_covered(arr[i], arr[j])])

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())

    arr = list(map(int, sys.stdin.readline().strip().split()))
    sol = Solution()
    result = sol.play_game(arr)
    print(result)