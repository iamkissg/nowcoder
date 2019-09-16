import sys


'''
题解: 共 n/(2m) 组,
     每一组的长度是 2m, 而每次的求和是 m(对应的正负数差)*m(元素个数)
'''


for line in sys.stdin:
    n, m = map(int, line.strip().split())
    print(int(n * m / 2))