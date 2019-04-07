import sys

NM = None
picture = []

for line in sys.stdin:
    if not NM:
        NM = line.strip().split()
        N, M = map(int, NM)
        continue
    if len(picture) < N:
        picture.append(line.strip())
        if len(picture) != N:
            continue
    print(picture)


    NM = None
    pic = []