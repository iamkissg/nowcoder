import sys

K = None

for line in sys.stdin:
    if not K:
        K = int(line.strip())
        continue
    A, X, B, Y = [int(a) for a in line.strip().split()]

    if A + B == K:
        print(X * Y)
    elif A * X + B * Y == K:
        print(1)
    elif A * X + B * Y < K:
        print(0)
    else:
        """时间问题, 先不处理"""
        print(1)

    K = None