import sys

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
    def can_return(self, pos, direction, instructions):
        if len(instructions) == 0 or 'G' not in instructions:
            return 'Y'
        
        steps = []
        for it in instructions:
            if it == 'G':
                steps.append(Gs[direction])
            elif it in {'L', 'R'}:
                direction = Ds[direction][it]

        pre_steps = {steps[0]}
        for st in (steps*2)[1:]:
            if st == (0, 1):
                if (0, -1) in pre_steps:
                    pre_steps.remove((0, -1))
                else:
                    pre_steps.add(st)
            elif st == (0, -1):
                if (0, 1) in pre_steps:
                    pre_steps.remove((0, 1))
                else:
                    pre_steps.add(st)
            elif st == (1, 0):
                if (-1, 0) in pre_steps:
                    pre_steps.remove((-1, 0))
                else:
                    pre_steps.add(st)
            elif st == (-1, 0):
                if (1, 0) in pre_steps:
                    pre_steps.remove((1, 0))
                else:
                    pre_steps.add(st)
            if len(pre_steps) == 0:
                return 'Y'
        else:
            return 'N'

if __name__ == "__main__":
    sol = Solution()
    instructions = input()
    print(sol.can_return([0, 0], 'N', instructions))