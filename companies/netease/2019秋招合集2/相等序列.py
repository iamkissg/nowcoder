import sys

# 100%

def can_we(nums):
    unique_nums = set(nums)
    if len(unique_nums) < 3:
        return True
    elif len(unique_nums) == 3:
        return True if sum(unique_nums) / len(unique_nums) in unique_nums else False
    else:
        return False


if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())

    for _ in range(k):
        n = int(sys.stdin.readline().strip())
        nums = list(map(int, sys.stdin.readline().strip().split()))
        print('YES' if can_we(nums) else 'NO')
