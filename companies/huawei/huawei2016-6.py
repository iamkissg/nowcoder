import sys
from copy import deepcopy
from queue import deque


for line in sys.stdin:
    n = line.strip()
    print(int(n, base=16))