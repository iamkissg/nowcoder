import sys
from copy import deepcopy
from queue import deque


for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        exit
    if n < 3:
        print(1)
    a, b = divmod(n, 3)
    c = a
    while a + b > 1:
        if a + b in (2, 3):
            print(c + 1)
            break
        a, b = divmod(a + b, 3)
        c += a