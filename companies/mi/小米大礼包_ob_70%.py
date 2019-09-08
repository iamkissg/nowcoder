def comb_gifts(prices, cost):
    global memo

    if len(prices) == 0:
        raise ValueError('No gifts')

    if cost < 0:
        return 0
    if len(prices) == 1:
        result = int(prices[0] == cost)
        memo[(str(prices), cost)] = result
        return result

    if cost in set(prices) or sum(prices) == cost:
        memo[(str(prices), cost)] = 1
        return 1
    elif sum(prices) < cost:
        memo[(str(prices), cost)] = 0
        return 0
    else:
        result = 0
        for i, p in enumerate(prices[:]):
            if p > cost:
                continue
            elif p == cost:
                memo[(str(prices), cost)] = result
                return 1
            result = result ^ comb_gifts(prices[:i]+prices[i+1:], cost-p)
            if result == 1:
                memo[(str(prices), cost)] = result
                return 1
            # return comb_gifts(prices[:i]+prices[i+1:], cost-prices[i])
        # if any([comb_gifts(prices[:i]+prices[i+1:], cost-prices[i]) for i, p in enumerate(prices)]):
        #     memo[(str(prices), cost)] = 1
        #     return 1
        # else:
        #     memo[(str(prices), cost)] = 0
        #     return 0
        else:
            return result

memo = {}

N = int(input())

prices = sorted(list(map(int, input().split())), reverse=True)
assert len(prices) == N

M = int(input())

print(comb_gifts(prices, M))