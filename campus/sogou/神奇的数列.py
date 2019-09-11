import sys

memo = {}

def where_are_you(i, j, t):
    si = i
    sj = j
    global memo

    if (i, j, t) in memo:
        return memo[(i, j, t)]
    
    c = 2
    while j < t:
        tmp = j
        j = i+j
        i = tmp
        c += 1
    if j == t:
        memo[(si, sj, t)] = c
        return c
    else:
        memo[(si, sj, t)] = -1
        return -1
    

for line in sys.stdin:
    x = int(line.strip())
    
    d = {}
    for i in range(1, x):
        for j in range(1, x):
            if i + j > x:
                continue
            arr = where_are_you(i, j, x)
            if arr != -1:
                if arr not in d:
                    d[arr] = 0
                d[arr] += 1


    d = sorted(d.items())
    for item in d:
        print(item[0], item[1])