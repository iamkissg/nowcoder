# 合并重叠字典
# 20190919
# 全部通过


def is_overlapped(a, b):
    # 题设 end 是开区间
    return a[0] <= b[1] and b[0] <= a[1]

def merge_overlapping_intervals(a, b):
    return [min(a[0], b[0]), max(a[1], b[1])]


def solute(pairs):
    if len(pairs) == 1:
        return pairs
    
    pairs = sorted(pairs, key=lambda t: (t[0], t[1]))
    while any([is_overlapped(i, j) for i, j in zip(pairs[:-1], pairs[1:])]):
        new_pairs = []
        i = 0
        while i < len(pairs)-1:
            if is_overlapped(pairs[i], pairs[i+1]):
                new_pairs.append(merge_overlapping_intervals(pairs[i], pairs[i+1]))
                i += 2
            else:
                new_pairs.append(pairs[i])
                i += 1

            if i == len(pairs) - 1:
                new_pairs.append(pairs[i])
        pairs = sorted(new_pairs, key=lambda t: (t[0], t[1]))

        if len(pairs) == 1:
            break
    return pairs


N = int(input())
pairs = [list(map(int, input().split())) for _ in range(N)]
result = solute(pairs)
for p in result:
    print(p[0], p[1])
