N = int(input())


unique_nums = set()
nums = []
for _ in range(N):
    n = int(input())
    nums.append(n)
    unique_nums.add(n)

memo = set()

internals = None
p1, p2 = 0, len(unique_nums)
while p1 <= len(nums)-len(unique_nums):
    if str(nums[p1: p2]) in memo:
        if internals is None:
            internals = [[p1+1, p2]]
        else:
            if internals[0][1]-internals[0][0] == p2-p1-1:
                internals.append([p1+1, p2])
            elif internals[0][1]-internals[0][0] > p2-p1-1:
                internals = [[p1+1, p2]]
    elif not unique_nums.difference(set(nums[p1: p2])):
        if internals is None:
            internals = [[p1+1, p2]]
        else:
            if internals[0][1]-internals[0][0] == p2-p1-1:
                internals.append([p1+1, p2])
            elif internals[0][1]-internals[0][0] > p2-p1-1:
                internals = [[p1+1, p2]]
        memo.add(str(nums[p1: p2]))
    else:
        while unique_nums.difference(set(nums[p1: p2])) and p2 < len(nums):
            p2 += 1
        else:
            if not unique_nums.difference(set(nums[p1: p2])):
                if internals is None:
                    internals = [[p1+1, p2]]
                else:
                    if internals[0][1]-internals[0][0] == p2-p1-1:
                        internals.append([p1+1, p2])
                    elif internals[0][1]-internals[0][0] > p2-p1-1:
                        internals = [[p1+1, p2]]
                memo.add(str(nums[p1: p2]))
    p1 += 1

print(internals[0][1]-internals[0][0]+1, len(internals))
print(' '.join(['['+str(it[0])+','+str(it[1])+']' for it in internals]))