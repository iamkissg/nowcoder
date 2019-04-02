import sys


for line in sys.stdin:
    s = line.strip()
    print(eval(s))