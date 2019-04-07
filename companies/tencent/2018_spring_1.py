import sys


for line in sys.stdin:
    n, m = map(int, line.strip().split())
    print(int(n * m / 2))