import sys


class Solution:
    def __init__(self):
        self.mapping = {
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15,
        }
    
    def convert_hex_to_dec(self, hex):
        res = 0
        for i, c in enumerate(hex[-1:1:-1]):
            res += (int(c) if c.isdigit() else self.mapping[c]) * 16**i
        return res


if __name__ == "__main__":
    sol = Solution()
    
    for line in sys.stdin:
        print(sol.convert_hex_to_dec(line.strip()))