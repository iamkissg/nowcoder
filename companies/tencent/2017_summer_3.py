import sys
from itertools import product, combinations


for line in sys.stdin:
    if ' ' not in line:
        continue
    nums = [int(s) for s in line.strip().split()]
    differences = {}
    for a, b in combinations(nums, 2):
        if str(abs(a-b)) not in differences:
            differences[str(abs(a-b))] = 0
        differences[str(abs(a-b))] += 1

    sorted_differences = sorted(differences.items(), key=lambda t: int(t[0]))
    print(sorted_differences[0][1], sorted_differences[-1][1])