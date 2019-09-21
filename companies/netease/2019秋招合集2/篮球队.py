import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(n, arr)