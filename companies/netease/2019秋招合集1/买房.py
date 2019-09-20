t = int(input())


for i in range(t):
    n, k = map(int, input().split())
    if k < 2:
        print(0, 0)
        continue
    mmin = 0
    mmax = k-1 if k <= n/2 else n-k
    print(mmin, mmax)