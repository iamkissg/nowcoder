import sys

class Solution:

    def __init__(self):
        self.memo = {}

    def coins(self, nums, target):
        if target <= 0:
            return [[]]

        result = []
        for n in nums:
            if target == n:
                result.append([n])
            elif target < n:
                continue
            else:
                result.extend([sorted(c+[n]) for c in self.coins(nums, target-n)])
        unique_result = []
        for res in result:
            if res in unique_result:
                continue
            unique_result.append(res)
        return unique_result

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 5]
    target = 10
    combinations = sol.coins(nums, target)
    for comb in combinations:
        print(comb)