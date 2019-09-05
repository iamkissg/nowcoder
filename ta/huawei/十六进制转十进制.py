# 也可以规划滑动窗口类型问题



import sys

mapping = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    }

for line in sys.stdin:
    line = line.strip()
    
    i = 0
    val = 0
    for c in line[-1:1:-1]:
        val += mapping[c] * 16 ** i
        i += 1
    print(val)