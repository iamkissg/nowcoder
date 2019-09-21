

# 100%

import sys
from functools import reduce

def find_least_common_multiple(a, b):
    s=a*b
    while a%b!=0:
        a, b=b, a%b
    return s//b
    # print(b,'is the maximum common divisor')
    # print(s//b,'is the least common multiple')


if __name__ == "__main__":
    
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    least_common_multiple = reduce(find_least_common_multiple, nums)
    m = least_common_multiple - 1
    print(sum([m%a for a in nums]))
