# 20190919
# 答案错误:您提交的程序没有通过所有的测试用例
# case通过率为60.00%

class Solution:

    def __init__(self):
        self.memo = {}


    def build(self, N, x, y, z):
        if N < x:
            return 0
        if N in {x, y, z}:
            return 1
        if (N, x, y, z) in self.memo:
            return self.memo[(N, x, y, z)]
        
        if (N-x, x, y, z) in self.memo:
            N_x = self.memo[(N-x, x, y, z)]
        else:
            N_x = self.build(N-x, x, y, z)
            self.memo[(N-x, x, y, z)] = N_x

        if (N-y, x, y, z) in self.memo:
            N_y = self.memo[(N-y, x, y, z)]
        else:
            N_y = self.build(N-y, x, y, z)
            self.memo[(N-y, x, y, z)] = N_y

        if (N-z, x, y, z) in self.memo:
            N_z = self.memo[(N-z, x, y, z)]
        else:
            N_z = self.build(N-z, x, y, z)
            self.memo[(N-z, x, y, z)] = N_z
            
        return N_x + N_y + N_z

    
N = int(input())

x, y, z = map(int, input().split())

sol = Solution()
result = sol.build(N, x, y, z)
print(result)