# 运行时间：46ms
# 占用内存：3504k


import sys
import math


def get_prime_factors(num, pf=3):
    if num % 2 == 0:
        return [2] + get_prime_factors(num // 2)
    else:
        # 使用 floor + 1, 是为了 sqrt(n) 刚好是整数时, 能取到该值, 比如 sqrt(9) == 3
        for i in range(pf, math.floor(math.sqrt(num))+1, 2):
            if num % i == 0:
                return [i] + get_prime_factors(num//i, pf=i)
        else:
            return [num] if num != 1 else []


for line in sys.stdin:
    n = int(line.strip())

    if n == 1:
        raise ValueError('1 既不是素数也不是合数.')
    elif n == 2:
        print('2 ')
    else:
        prime_factors = get_prime_factors(n)
        print(' '.join(map(str, prime_factors))+' ')