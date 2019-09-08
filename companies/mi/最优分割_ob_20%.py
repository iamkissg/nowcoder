from typing import List


def split(nums: List[int], T: int):
    global memo

    if len(nums) == T:
        memo[(str(nums), T)] = max(nums)
        return max(nums)
    elif T == 1:
        memo[(str(nums), T)] = max(nums)
        return max(nums)


    else:
        # print(len(nums)-T)
        minmax = []
        for pos in range(1, len(nums)-T+1):
            # print(pos, nums[:pos], nums[pos:], T-1)
            tmp = max([sum(nums[:pos]), split(nums[pos:], T-1)])
            # print(tmp)
            # memo[(str(nums), T)] = tmp
            minmax.append(tmp)
        # print(minmax)
        return min(minmax)



memo = {}

N, M = map(int, input().split())
assert N >= M

nums = list(map(int, input().split()))
assert len(nums) == N

print(split(nums, M))