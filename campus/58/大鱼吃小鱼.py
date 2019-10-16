import sys


class Solution:

    def eat(self, F, m):
        F.sort()

        for _ in range(m):
            min_val = F[0]
            tmp = []
            for i, v in enumerate(F[1:], start=1):
                if v != min_val:
                    tmp.append(v+min_val)
                    tmp.extend(F[i+1:])
                    break
                else:
                    tmp.append(v)
            F = tmp
            F.sort()
        
        return F[0]

if __name__ == "__main__":
    sol = Solution()

    arr = list(map(int, input().split()))
    n, m, F = arr[0], arr[1], arr[2:]
    print(sol.eat(F, m))