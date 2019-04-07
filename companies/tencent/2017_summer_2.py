import sys

"""ACCEPT"""

for line in sys.stdin:
    s = line.strip()
    print(''.join(sorted(s, key=lambda w: w >= 'a', reverse=True)))