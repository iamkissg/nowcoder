import sys
import re
from string import ascii_letters


class Solution:

    def sum_distance(self, arr):
        dist = []
        for s in arr:
            if len(s) <= 1:
                dist.append(0)
            elif all([c in ascii_letters for c in s]):
                d = abs(ord(s[0])-ord(s[-1]))
                dist.append(d)
                
        return sum(dist)
            
    # def get_distance(self, s):
    #     sub_str = re.findall('[A-Za-z]*', s)
    #     dist = 0
    #     for sub in sub_str:
    #         if not s:
    #             continue
    #         dist += ord()



if __name__ == "__main__":
    sol = Solution()

    for line in sys.stdin:
        arr = line.strip().split(';')
        print(sol.sum_distance(arr))