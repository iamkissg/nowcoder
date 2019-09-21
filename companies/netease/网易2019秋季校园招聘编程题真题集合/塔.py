import sys

# 100% passed

def is_balanced(towers):
    return max(towers) == min(towers)


def balance_towers(towers, k):
    n_opt = 0
    opts = []
    for _ in range(k):
        idx_max = towers.index(max(towers))
        idx_min = towers.index(min(towers))
        towers[idx_max] -= 1
        towers[idx_min] += 1
        n_opt += 1
        opts.append((idx_max+1, idx_min+1))
        if is_balanced(towers):
            break
    return max(towers)-min(towers), n_opt, opts


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())
    towers = list(map(int, sys.stdin.readline().strip().split()))
    s, m, opts = balance_towers(towers, k)
    print(s, m)
    for x, y in opts:
        print(x, y)