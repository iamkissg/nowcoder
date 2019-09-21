import sys

# def can_we(hs, m):
#     n_h = len(hs)
#     if m + sum(hs) > (n_h-1)*n_h/2:
#         return True
#     else:
#         return False

def can_we(hs, m):
    n_h = len(hs)
    if m + sum(hs) < (n_h-1)*n_h/2:
        return False
    
    for i, h in enumerate(hs):
        if h >= i:
            m += h-i
            hs[i] = i
        else:
            if m < i-h:
                return False
            hs[i] += i-h
            m -= i-h
    # print(hs)
    return True


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        n, m = map(int, sys.stdin.readline().strip().split())
        hs = list(map(int, sys.stdin.readline().strip().split()))
        if can_we(hs, m):
            print('YES')
        else:
            print('NO')