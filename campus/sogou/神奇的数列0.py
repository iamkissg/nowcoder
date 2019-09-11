import sys


def generate_array(i, j, t):
    arr = [i, j]
    while j < t:
        tmp = j
        j = i+j
        i = tmp
        arr.append(j)
    return arr
    


for line in sys.stdin:
    x = int(line.strip())
    
    d = {}
    for i in range(1, x):
        for j in range(1, x):
            arr = generate_array(i, j, x)
            if x in arr:
                if arr.index(x)+1 not in d:
                    d[arr.index(x)+1] = 0
                d[arr.index(x)+1] += 1

    d = sorted(d.items())
    for item in d:
        print(item[0], item[1])