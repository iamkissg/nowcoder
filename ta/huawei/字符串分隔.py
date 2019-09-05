# 依然是子串问题, 只要满足条件, 即可输出子串


import sys


for line1 in sys.stdin:
    line1 = line1.strip()
    line2 = input().strip()

    Eights = []
    for line in [line1, line2]:
        eight = ''
        for i, c in enumerate(line, start=1):
            eight += c
            if i % 8 == 0:
                Eights.append(eight)
                eight = ''
        else:
            if eight != '' and len(eight) < 8:
                eight += '0' * (8-len(eight))
                Eights.append(eight)
    
    for e in Eights:
        print(e)