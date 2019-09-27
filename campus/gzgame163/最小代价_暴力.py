import sys
from itertools import permutations

class Solution:
    
    keyboards = list([''.join(p) for p in permutations('ASDFGH', 6)])

    def least_cost(self, s: str):
        if len(s) == 1:
            return 0
        
        costs = [[0] for _ in range(len(self.keyboards))]

        for j, keyboard in enumerate(self.keyboards):
            pre_pos = keyboard.index(s[0])
            for i, c in enumerate(s[1:], start=1):
                cur_pos = keyboard.index(c)
                costs[j].append(pre_pos-cur_pos)
                pre_pos = cur_pos
        costs = [sum(map(abs, c)) for c in costs]
        # min_index = costs.index(min(costs))
        # print(self.keyboards[min_index])
        # print(costs[min_index])
        return min(costs)


if __name__ == "__main__":
    sol = Solution()

    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        s = sys.stdin.readline().strip()
        print(sol.least_cost(s))
