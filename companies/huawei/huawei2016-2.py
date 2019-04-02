import sys
from copy import deepcopy
from queue import deque


for line in sys.stdin:
    inp = line.strip()
    outp = []
    for c in inp:
        if c not in outp:
            outp.append(c)
    print("".join(outp))