#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。

# 70%

import sys
from string import ascii_uppercase

class Solution:
    def __init__(self, names):
        self.names = names

    def find_name(self, yes, no):
        ok_names = {name for name in self.names if not name.startswith(no) and name.startswith(yes)}
        if ok_names:
            result = sorted(ok_names)[0]
            self.names.remove(result)
            return result
        else:
            return '-1'

if __name__ == "__main__":
    # 读取第一行的n
    n, m = map(int, sys.stdin.readline().strip().split())
    
    names = {sys.stdin.readline().strip() for _ in range(n)}
    sol = Solution(names)
    for _ in range(m):
        yes, no = sys.stdin.readline().strip().split()
        print('give you', sol.find_name(yes, no))