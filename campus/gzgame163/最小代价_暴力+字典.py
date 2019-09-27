import sys
from itertools import permutations



class Solution:
    
    keyboards = [{c: i for i, c in enumerate(p)} for p in permutations('ASDFGH', 6)]

    def least_cost(self, s: str):
        if len(s) == 1:
            return 0
        
        costs = [[keyboard[s[0]]] for keyboard in self.keyboards]

        for k, keyboard in enumerate(self.keyboards):
            costs[k] += [keyboard[i]-keyboard[j] for i, j in zip(s[1:], s[:-1])]

        costs = [sum(map(abs, c)) for c in costs]
        return min(costs)


if __name__ == "__main__":
    sol = Solution()

    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        s = sys.stdin.readline().strip()
        print(sol.least_cost(s))
