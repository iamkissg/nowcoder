import sys
from copy import deepcopy
from queue import deque


for line in sys.stdin:
    n = int(line.strip())
    if n > 1000:
    n = 999
    a = deque(range(n))
    # print('a', a)
    c = 0  # counter
    while len(a) > 1:
        x = a.popleft()
        if c % 3 == 2:
            pass
        else:
            a.append(x)
            # print('a', a)
            # print('b', b)
        c += 1
        # print('a', a)
    print(a.popleft())