import sys
from collections import Counter

class Solution:

    def int2list(self, num):
        result = []
        while num:
            num, mod = divmod(num, 10)
            result.append(mod)
        return result[::-1]

    def do_homework(self, a, b):
        counter = Counter()

        a_list = self.int2list(a)
        b_list = self.int2list(b)
        counter.update(a_list)
        counter.update(b_list)

        for n in b_list[::-1]:
            n_list = a*n
            counter.update(self.int2list(n_list))
        
        counter.update(self.int2list(a*b))

        return counter



if __name__ == "__main__":
    sol = Solution()

    N = int(sys.stdin.readline().strip())
    counter = Counter()

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().strip().split())
        c = sol.do_homework(a, b)
        print(' '.join(map(str, [c.get(k, 0) for k in [1, 2, 3, 4, 5, 6, 7, 8, 9]])))
        counter.update(c)
    
    counter.pop(0)
    lucky_number, _ = counter.most_common(1)[0]
    print(lucky_number)