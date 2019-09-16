import sys

n = None

for line in sys.stdin:
    if not n:
        n = int(line.strip())
        continue
    cards = [int(a) for a in line.strip().split()]

    assert n == len(cards)

    if n == 0:
        print(0)
    elif n == 1:
        print(cards[0])
    elif n == 2:
        print(abs(cards[0] - cards[1]))
    else:
        sorted_cards = sorted(cards, reverse=True)
        if n % 2:  # 1
            res = sorted_cards[-1]
            for i in range(0, n-1,  2):
                res += sorted_cards[i] - sorted_cards[i+1]
        else:
            res = 0
            for i in range(0, n, 2):
                res += sorted_cards[i] - sorted_cards[i+1]
        print(res)
    n = None