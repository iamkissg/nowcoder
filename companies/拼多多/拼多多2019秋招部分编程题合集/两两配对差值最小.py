import sys

# 100% passed

class Solution:

    def combine_numbers(self, numbers):
        numbers.sort()
        start, end = 0, len(numbers)-1

        combinations = set()
        while start < end:
            combinations.add(numbers[start]+numbers[end])
            start += 1
            end -= 1
        return max(combinations)-min(combinations)

        


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    numbers = list(map(int, sys.stdin.readline().strip().split()))
    sol = Solution()
    print(sol.combine_numbers(numbers))
    print(sol.combine_numbers([2, 6, 4, 3]))
    print(sol.combine_numbers([11, 4, 3, 5, 7, 1]))
    print(sol.combine_numbers([1, 3, 5, 6, 7, 9]))