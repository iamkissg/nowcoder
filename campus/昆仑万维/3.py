from typing import List
from functools import cmp_to_key

import sys

class Solution:
    def sign_sort(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda t: t>0)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    print(' '.join(map(str, sol.sign_sort(arr))))