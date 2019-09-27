import sys
from itertools import permutations

class Solution:
    
    keyboard = 'ASDFGH'

    def least_cost(self, s: str):
        if len(s) == 1:
            return 0
        
        costs = [0]
        pre_pos = self.keyboard.index(s[0])
        for i, c in enumerate(s[1:], start=1):
            cur_pos = self.keyboard.index(c)
            costs.append(pre_pos-cur_pos)
            pre_pos = cur_pos
        cost = sum(map(abs, costs))
        return cost


if __name__ == "__main__":
    sol = Solution()

    print(len(list(permutations('ASDFGH', 6))))
    # T = int(sys.stdin.readline().strip())

    # for _ in range(T):
    #     s = sys.stdin.readline().strip()
    #     print(sol.least_cost(s))
