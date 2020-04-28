import sys

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
                steps.append(direction)
            elif it in {'L', 'R'}:
                direction = Ds[direction][it]

        pre_steps = [steps[0]]
        rest_steps = (steps*2)[1:]
        for st in rest_steps:
            if st == 'N':
                if 'S' in pre_steps:
                    pre_steps.remove('S')
                else:
                    pre_steps.append(st)

            elif st == 'S':
                if 'N' in pre_steps:
                    pre_steps.remove('N')
                else:
                    pre_steps.append(st)

            elif st == 'E':
                if 'W' in pre_steps:
                    pre_steps.remove('W')
                else:
                    pre_steps.append(st)
                    
            elif st == 'W':
                if 'E' in pre_steps:
                    pre_steps.remove('E')
                else:
                    pre_steps.append(st)

            if len(pre_steps) == 0:
                return 'Y'
        else:
            return 'N'

if __name__ == "__main__":
    sol = Solution()
    instructions = input()
    print(sol.can_return([0, 0], 'N', instructions))