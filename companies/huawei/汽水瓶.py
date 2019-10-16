import sys


for line in sys.stdin:
    if line == '0\n':
        break
    n = int(line.strip())
    if n >=2:
        print(n//2)
    else:
        print(0)