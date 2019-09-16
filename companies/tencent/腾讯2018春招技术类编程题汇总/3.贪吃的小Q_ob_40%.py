import sys
from math import ceil, floor

for line in sys.stdin:
    """有问题"""
    N, M = map(int, line.strip().split())
    remain = int(floor((M - N) / 2))
    res = remain
    while True:
        if remain % 2:
            remain = remain // 2 + 1
        else:
            remain = remain // 2
            res += 1
        if remain == 1:
            break
    print(res+1 if M % 2 else res)