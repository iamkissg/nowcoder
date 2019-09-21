import sys
from math import factorial


def find_kth_word(n, m, k):
    if factorial(n+m)/(factorial(m)*factorial(n)) < k:
        return None


if __name__ == "__main__":
    n, m, k = map(int, sys.stdin.readline().strip().split())
    print(n, m, k)