import sys
from copy import deepcopy
from queue import deque


for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        a, b = 1, 1
        for i in range(1, n-1):
            a, b = b, a+b
        print(b)
            