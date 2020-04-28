#coding=utf-8
import sys

class Solution:
    def func(self, s: str):
        if not s:
            return []
        
        res = []
        n = len(s)
        mid = n // 2
        # 奇数
        if n & 1:
            l, r = mid - 1, mid+1
            res.append(s[mid])
        else:
            l, r = mid - 1, mid
        
        i = 1
        while l-i >= 0:
            if s[l-i:l] == s[r:r+i]:
                res = [s[l-i:l+1]] + res + [s[r:r+i+1]]
                l, r = l-i, r+i
                i = 1
            else:
                i += 1
        if sum([len(c) for c in res]) < n:
            return [s]
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.func('abcdefdeabc'))