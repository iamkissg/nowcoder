import sys
if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())
    arr = sorted({int(s) for s in sys.stdin.readline().strip().split() if s != '0'}, reverse=True)
    som = 0

    if not arr:
        for i in range(k):
            print(0)
    else:
        for i in range(k):
            if arr:
                a = arr.pop()
                if a != 0:
                    print(a-som)
                    som += a
                elif a == 0 and arr:
                    a = arr.pop()
                    print(a-som)
                    som += a
                else:
                    print(0)
            else:
                print(0)