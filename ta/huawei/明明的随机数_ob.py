# 运行时间：59ms
# 占用内存：4812k


import sys
from copy import deepcopy
from queue import deque


for line in sys.stdin:
    n = int(line.strip())
    l = set()
    for i in range(n):
        ins = input()
        l.add(int(ins.strip()))
    print('\n'.join(map(str, sorted(l))))