from typing import List

import sys
from string import ascii_letters as letters

'''
20191027
只交换字母, 不交换特殊字符
'''

class Solution:
    def swap_letters(self, s: List[str]) -> str:
        if not s:
            return ''
        
        n = len(s)
        l, r = 0, n-1
        while l < r:
            if s[l] not in letters:
                l += 1
                continue
            if s[r] not in letters:
                r -= 1
                continue
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
        return ''.join(s)

if __name__ == "__main__":
    sol = Solution()
    s = input()
    print(sol.swap_letters(list(s)))