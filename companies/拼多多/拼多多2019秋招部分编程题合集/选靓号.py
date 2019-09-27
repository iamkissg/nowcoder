import sys


'''
修改没有思路
'''

class Solution:
    def __init__(self):
        self.memo = {}


    def phone_number_cost(self, p1, p2):
        return sum(map(abs, [i-j for i, j in zip(p1, p2)]))
    
    number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    def least_cost(self, phone_number, k):
        included = set(phone_number)

        i2lc = {}
        for i in self.number:
            i_costs = list(map(abs, [phn-i for phn in phone_number]))
            i_costs.sort()
            i2lc[i] = sum(i_costs[:k])

        least_cost = min(i2lc.values())
        nums = [i for i in i2lc if i2lc[i] == least_cost]
        n_need_to_change = {n: k-phone_number.count(n) for n in nums}
        n_need_to_change2 = {k: [phn for phn in phone_number if phn != k] for k in nums}

        for k, v in n_need_to_change2.items():
            times = n_need_to_change[k]

        # candicates = {for k, v in n_need_to_change.items() }
        # for k, v in n_need_to_change.items():


        return least_cost


if __name__ == "__main__":
    sol = Solution()

    N, K = map(int, sys.stdin.readline().strip().split())
    phone_number = list(map(int, sys.stdin.readline().strip()))

    print(sol.least_cost(phone_number, K))