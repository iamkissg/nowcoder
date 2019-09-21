import sys

# 100% passed

def find_max(arr):
    a, b, c = arr

    return max([a+b+c, a*b*c, (a+b)*c, a*(b+c), a+b*c, a*b+c])


if __name__ == "__main__":
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(find_max(arr))