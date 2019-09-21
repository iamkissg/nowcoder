import sys
from itertools import chain

# 运行超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。
# case通过率为90.00%

def gen_prime_nums():
    prime_nums = []
    is_not_prime = set()
    for i in range(2, 2**16):
        if i not in is_not_prime:
            prime_nums.append(i)
            is_not_prime.update({j for j in range(i, 2**16, i)})
    return prime_nums


class Solution:

    prime_nums = gen_prime_nums()
    memo = {}

    def ngcd(self, nums):
        ok_prime = set()
        for num in nums:
            if num in self.memo:
                ok_prime.update(self.memo[num])
                continue
            else:
                this_ok_prime = set()
                for pn in self.prime_nums:
                    if num % pn == 0:
                        this_ok_prime.add(pn)
                    if pn > num: break
                ok_prime.update(this_ok_prime)
                self.memo[num] = this_ok_prime

        return ok_prime



if __name__ == "__main__":
    sol = Solution()

    n = int(sys.stdin.readline().strip())
    pairs = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    # mins = [[min(p)] for p in pairs]
    # ok_primes = [sol.ngcd(p) for p in mins]
    ok_primes = [sol.ngcd(p) for p in pairs]

    ngcd = ok_primes[0].intersection(*ok_primes)
    if not ngcd:
        print(-1)
    else:
        print(max(ngcd))
