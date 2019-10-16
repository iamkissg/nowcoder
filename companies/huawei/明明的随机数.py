import bisect
import sys


for line in sys.stdin:
    N = int(line.strip())
    # res = [-sys.maxsize]
    res = []
    for _ in range(N):
        i = int(input())
        if i not in res:
            bisect.insort_left(res, i)
    print('\n'.join(map(str, res)))