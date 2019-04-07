import sys

for line in sys.stdin:
    N, K = map(int, line.strip().split())
    if K == 0:
        print(N)
    elif N == 1:
        print(1)
    else:
        from math import log2
        splitn = min(K, int(log2(N)))
        for _ in range(splitn):
            N = (N+1)//2
        print(N+splitn)