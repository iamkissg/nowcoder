class Solution:

    def __init__(self):
        self.memo = {}

    def split_number(self, T):
        # 递归+记忆化
        if T == 1:
            return {(1,)}
        if T == 2:
            return {(1,1), (2,)}

        if T in self.memo:
            return self.memo[T]

        result = {(T,)}
        for i in range(1, T//2+1):
            result.update({tuple(sorted((i,)+item)) for item in self.split_number(T-i)})
        
        self.memo[T] = result
        return result


while True:
    sol = Solution()

    T = int(input())
    result = sorted(sol.split_number(T))
    for item in result:
        print('+'.join(map(str, item)))