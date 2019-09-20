costs = sorted([int(i) for i in input().split()], reverse=True)

print(sum([abs(i-j) for i, j in zip(costs[:-1], costs[1:])]))