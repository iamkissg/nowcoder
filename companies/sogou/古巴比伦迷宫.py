from operator import xor
from collections import Counter


def logical_xor(a, b):
    return bool(a) ^ bool(b)


def pass_or_not(pans, M):
    if not any(pans):
        return False

    max_len = len(bin(max(pans)))-2
    bitmap = [[0 for col in range(max_len)] for row in range(len(pans))]
    bitmap_T = [[0 for col in range(len(pans))] for row in range(max_len)]
    for ip, p in enumerate(pans):
        for ib in range(max_len):
            bitmap[ip][ib] = p >> ib & 1
            bitmap_T[ib][ip] = p >> ib & 1
    if any([Counter(bm)[1]==1 for bm in bitmap_T]):
        return False
    # elif some_condition:
    #     pass
    else:
        return True

T = int(input())


for _ in range(T):
    M, N = map(int, input().split())
    pans = [int(input(), base=16) for _ in range(N)]

    if pass_or_not(pans, M):
        print('yes')
    else:
        print('no')