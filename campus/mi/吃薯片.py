# 本题有一丢丢没解释清楚的
# 输出写道, Yes代表小米是快乐值最大的. 而题目描述中是预测小米是否会成为赢家(快乐值相同时, 小米赢)
# 因此, 假定, Yes代表小米是快乐值最大的 (包括相同快乐值的情况)

from math import ceil

def max_hp(accumulated, rest, threshold):    

    global memo
    if str(rest) in memo:
        return memo[str(rest)]

    if len(rest) == 1:
        memo[str(rest)] = rest[0]
        return rest[0]
    elif len(rest) == 2:
        memo[str(rest)] = max(rest)
        return max(rest)
    else:
        min_hp = accumulated + min([
            max_hp(accumulated+rest[0], rest[2:], threshold),
            max_hp(accumulated+rest[0], rest[1:-1], threshold),
            max_hp(accumulated+rest[-1], rest[1:-1], threshold),
            max_hp(accumulated+rest[-1], rest[:-2], threshold),
        ])
        memo[str(rest)] = min_hp
        return min_hp


memo = {}
happiness = list(map(int, input().split()))
sum_hp = sum(happiness)0gs

xiaomi_win = max_hp(0, happiness, None) * 2 >= sum_hp
print(max_hp(0, happiness, None), sum_hp)
print('Yes' if xiaomi_win else 'No')