# 测试用例通过 90%


n, m  = map(int, input().split())
pairs = [list(map(int, input().split())) for _ in range(n)]

counter = [0] * (m+1)                # 竞选者得票数, 数组表示
for p in pairs:
    counter[p[0]] += 1
# print(counter)
pairs = [p for p in pairs if p[0] != 1]
# print(pairs)

c = 0
while counter[1] <= max(counter[2:]):
    vailable_indexes = [p[0] for p in pairs]
    min_costs = sorted([p[1] for p in pairs])

    # 可能存在得票数相同的竞选者, 根据投票人的代价排序
    most_votes = sorted([(i, counter[i]) for i in vailable_indexes], key=lambda t: (t[1], -min([p[1] for p in pairs if p[0] == t[0]])), reverse=True)
    max_index = [i[0] for i in most_votes if i[0] in vailable_indexes][0]
    min_max_costs = sorted([p[1] for p in pairs if p[0] == max_index])

    if min_max_costs[0] == min_costs[0]:
        counter[max_index] -= 1
        counter[1] += 1
        c += min_max_costs[0]
        pairs.remove([max_index, min_max_costs[0]])
    else:
        # 能争取到两票
        if min_max_costs[0] != min_costs[1] and min_max_costs[0] < min_costs[0] + min_costs[1]:
            counter[max_index] -= 1
            counter[1] += 1
            c += min_max_costs[0]
            pairs.remove([max_index, min_max_costs[0]])
        else:
            valid_pairs = [[p[0], counter[p[0]]] for p in pairs if p[0] in vailable_indexes and p[1] == min_costs[0]]
            index = sorted(valid_pairs, key=lambda t: t[1], reverse=True)[0][0]
            counter[index] -= 1
            counter[1] += 1
            c += min_costs[0]
            pairs.remove([index, min_costs[0]])
print(c)