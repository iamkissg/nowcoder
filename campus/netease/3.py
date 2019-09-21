import sys


def can_we(hs, cur, k, super_power):

    # 可直接跳达 h_n
    if len(hs)-cur <= k:
        if super_power:
            return True
        elif hs[cur] >= hs[-1]:
            return True
        else:
            return False
    
    for i in k:
           



if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        n, k = map(int, sys.stdin.readline().strip().split())
        hs = list(map(int, sys.stdin.readline().strip().split()))
        if can_we(hs, cur=0, k=k, super_power=1):
            print('YES')
        else:
            print('NO')