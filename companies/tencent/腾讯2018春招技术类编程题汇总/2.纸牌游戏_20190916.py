import sys


'''
排序解法:
===

每个人都采用最优策略, 意味着每次都从取剩余纸牌中最大的那张
所以计数时, +牛牛-羊羊即可
'''

def get_max_score(cards):
    if len(cards) == 1:
        return cards[0]

    sorted_cards = sorted(cards, reverse=True)
    val = 0
    for i, c in enumerate(sorted_cards):
        if i & 1:
            val -= c
        else:
            val += c
    return val


n = int(input())

cards = list(map(int, input().split()))
assert len(cards) == n

score = get_max_score(cards)
print(score)
