# 相比不适用 memorization 的版本 (46ms), 快了近一倍
# 不是太清楚该在何处使用 memorization, 使用了 global, 有点粗糙
# 运行时间：26ms
# 占用内存：3432k

import sys
import math


def get_prime_factors(num, pf=3):
    global memorization

    # special case
    if num == 1:
        return []

    # print('memorization', memorization)
    if num in memorization:
        return memorization[num]

    if num % 2 == 0:
        prime_factors = [2] + get_prime_factors(num // 2)
        memorization[num] = prime_factors
        return prime_factors
    else:
        # 使用 floor + 1, 是为了 sqrt(n) 刚好是整数时, 能取到该值, 比如 sqrt(9) == 3
        for i in range(pf, math.floor(math.sqrt(num))+1, 2):
            if num % i == 0:
                prime_factors = [i] + get_prime_factors(num//i, pf=i)
                memorization[num] = prime_factors
                return prime_factors
        else:
            prime_factors = [num]
            memorization[num] = prime_factors
            return prime_factors

memorization = {}
for line in sys.stdin:
    n = int(line.strip())

    if n == 1:
        raise ValueError('1 既不是素数也不是合数.')
    elif n == 2:
        print('2 ')
    else:
        # dynamic programming
        # add memorization to accelerate program
        prime_factors = get_prime_factors(n)
        print(' '.join(map(str, prime_factors))+' ')