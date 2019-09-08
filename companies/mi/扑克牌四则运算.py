from typing import List

def cal_twenty_four(nums: List[int], target: int):

    if len(nums) == 2:
        a, b = nums[0], nums[1]
        if target in (a+b, a-b, b-a, a*b, a//b, b//a):
            print(target, nums, (a+b, a-b, b-a, a*b, a//b, b//a))
            return 1
        else:
             return 0

    for i, n in enumerate(nums):
        rest_nums = nums[:i] + nums[i+1:]
        print(rest_nums, target, n)
        # print(rest_nums, 'target-n', target-n, cal_twenty_four(rest_nums, target-n))
        # print(rest_nums, 'target+n', target+n, cal_twenty_four(rest_nums, target+n))
        # print(rest_nums, 'target//n', target//n, cal_twenty_four(rest_nums, target//n))
        # print(rest_nums, 'target*n', target*n, cal_twenty_four(rest_nums, target*n))
        # print(rest_nums, 'n//target', n//target, cal_twenty_four(rest_nums, n//target))
        print('target-n', target, n, target-n, rest_nums)
        if cal_twenty_four(rest_nums, target-n):
            return 1
        print('n-target', target, n, n-target, rest_nums)
        if cal_twenty_four(rest_nums, n-target):
            return 1
        print('target+n', target, n, target+n, rest_nums)
        if cal_twenty_four(rest_nums, target+n):
            return 1
        print('target*n', target, n, target*n, rest_nums)
        if cal_twenty_four(rest_nums, target*n):
            return 1
        # print('n//target', target, n, n//target, rest_nums)
        # if cal_twenty_four(rest_nums, n//target):
        #     return 1
    else:
        return 0




nums = list(map(int, input().strip().split()))
target = int(input())


print(cal_twenty_four(nums, target))