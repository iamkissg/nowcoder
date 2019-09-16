from math import factorial

class Solution(object):

    MOD = 1000000007

    def split_song(self, K, len_A, num_A, len_B, num_B):
        if len_A * num_A + len_B * num_B < K:
            return 0
        elif len_A * num_A + len_B * num_B == K:
            return 1

        if num_A == 0:
            if K % len_B:
                return 0
            else:
                m = K // len_B
                # print('AAA', K, len_B, num_B, (factorial(num_B) / (factorial(m) * factorial(num_B-m))))
                return (factorial(num_B) / (factorial(m) * factorial(num_B-m))) % self.MOD
        if num_B == 0:
            if K % len_A:
                return 0
            else:
                m = K // len_A
                # print('BBB', K, len_A, num_A, (factorial(num_A) / (factorial(m) * factorial(num_A-m))))
                return (factorial(num_A) / (factorial(m) * factorial(num_A-m))) % self.MOD
        
        result = 0
        if K - len_A > 0:
            result = (result+num_A*self.split_song(K-len_A, len_A, num_A-1, len_B, num_B)) % self.MOD
            # print('CCC', num_A*self.split_song(K-len_A, len_A, num_A-1, len_B, num_B))
        elif K - len_A == 0:
            # print(result)
            result = (result+num_A) % self.MOD

        if K - len_B > 0:
            result = (result+num_B*self.split_song(K-len_B, len_A, num_A, len_B, num_B-1)) % self.MOD
            # print('DDD', num_B, self.split_song(K-len_B, len_A, num_A, len_B, num_B-1))
        elif K - len_B == 0:
            result = (result+num_B) % self.MOD
            # print(result)

        # print(K, len_A, num_A, len_B, num_B, result)
        return result


K = int(input())
line = input()

len_A, num_A, len_B, num_B = [int(i) for i in line.split()]

sol = Solution()
n = sol.split_song(K, len_A, num_A, len_B, num_B)
print(n//2)

