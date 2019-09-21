import sys


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        a, b, c = list(map(int, sys.stdin.readline().strip().split()))
        print(a, b, c)