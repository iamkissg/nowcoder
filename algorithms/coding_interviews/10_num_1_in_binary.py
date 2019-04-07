# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n == 0:
            return 0
        
        # 对负数有问题
        # count = 0
        # while n:
        #     count += 1
        #     n = n & (n-1)
        # return count
        
        count = 0
        flag = 1
        for _ in range(32):  # 取巧了, 如果整数的位长不是 32 就出问题了
            if n & flag:
                count += 1
            flag = flag << 1
        return count

if __name__ == "__main__":
    import sys
    sol = Solution()
    print(sol.NumberOf1(-1))