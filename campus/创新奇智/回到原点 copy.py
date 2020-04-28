import sys
import time

Gs = {
    'N': (0, 1),
    'S': (0, -1),
    'W': (-1, 0),
    'E': (1, 0),
}
Ds = {
    'N': {'L': 'W', 'R': 'E'},
    'W': {'L': 'S', 'R': 'N'},
    'S': {'L': 'E', 'R': 'W'},
    'E': {'L': 'N', 'R': 'S'},
}

class Solution:
    def can_return(self, pos, direction, instructions, start_time):
        if pos == [0, 0] and (len(instructions) == 0 or 'G' not in instructions):
            return 'Y'
        elif pos != [0, 0] and len(instructions) == 0:
            return 'N'
        
        while time.time() - start_time < 0.5:
            for i, it in enumerate(instructions):
                if it == 'G':
                    pos = pos[0]+Gs[direction][0], pos[1]+Gs[direction][1]
                    if pos == [0, 0]:
                        return 'Y'
                elif it in {'L', 'R'}:
                    direction = Ds[direction][it]
        return 'N'


if __name__ == "__main__":
    sol = Solution()
    instructions = input()
    print(sol.can_return([0, 0], 'N', instructions, time.time()))