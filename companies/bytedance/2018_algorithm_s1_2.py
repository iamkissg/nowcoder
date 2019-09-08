import sys
from itertools import combinations


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    nums = list(map(int, sys.stdin.readline().strip().split()))
    d = {min(internal) * sum(internal): internal for internal in
        (internal for i in range(1, N+1) for internal in combinations(nums, i))}
    print(max(d))
    print(d[max(d)])
    print(max(map(
        lambda t: t[0]*t[1],
        [(min(internal), sum(internal)) for internal in
        (internal for i in range(1, N+1) for internal in combinations(nums, i))])))

