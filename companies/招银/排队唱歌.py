import sys
import bisect

class Solution:

    def count_by_bubble_sort(self, nums):
        # 60% passed
        result = 0
        length = len(nums)

        change = True
        while change:
            change = False
            for i in range(1, length):
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    result += 1
                    change = True
            length -= 1
        return result

    def count_by_naive_comparison(self, nums):
        '''
        20190923
        简单记录逆序对, 用了两重循环, 时间复杂度还是 O(n^2), 不满足题目要求
        但是切换成 C++, 同样的统计逆序对就通过了....
        '''
        result = 0
        for i, p in enumerate(nums[:-1]):
            for j, n in enumerate(nums[i:]):
                if p > n:
                    result += 1

        return result

    def merge_sort_helper(self, nums, count):
        if len(nums) == 1:
            return nums, count

        len_nums = len(nums)
        left = nums[:len_nums//2]
        right = nums[len_nums//2:]

        left, count = self.merge_sort_helper(left, count)
        right, count = self.merge_sort_helper(right, count)

        merged = []
        while left and right:
            if left[-1] > right[-1]:
                count += len(right)
                merged.append(left.pop())
            else:
                merged.append(right.pop())
        else:
            if left:
                merged.extend(left[::-1])
            else:
                merged.extend(right[::-1])

        return merged[::-1], count

    def count_by_merge_sort(self, nums):
        '''
        看到牛客好多提到归并排序来统计逆序对的, 原来剑指 offer 上就有这道题, 题36
        我以为 bisect 已经很快了 (100000 比前两者快多了), 和归并排序比起来还是差了一个数量级还多
        快, 真快, 无敌快
        '''
        if not nums or len(nums) == 1:
            return 0

        count = 0
        # 返回一个排序好的数组
        _, count = self.merge_sort_helper(nums, count)
        # print(sorted(nums)==sorted_nums)
        return count

    def count_by_bisecting(self, nums):
        '''
        这个方法是真快啊, 遍历nums O(n), 搜索插入位置 O(logn), 插入 O(n), 后面我就不会算了
        不过比较难以想到, 累加每个数字, 在当前数组和排序完的数组中的索引差
        画一画, 确实如此, 但是真挺反直觉的.
        '''
        result = 0
        sorted_nums = []
        for i, n in enumerate(nums):
            sorted_index = bisect.bisect_left(sorted_nums, n)
            bisect.insort_left(sorted_nums, n)
            result += abs(sorted_index-i)

        return result


if __name__ == "__main__":
    import time
    sol = Solution()

    N = int(sys.stdin.readline().strip())
    heights = [int(sys.stdin.readline().strip()) for _ in range(N)]
    print(sol.count_inversion_by_merge_sort(heights))

    

    start_time = time.time()
    heights = list(range(10000, 0, -1))
    # 3s
    print(sol.count_by_naive_comparison(heights))
    print(time.time()-start_time)

    start_time = time.time()
    heights = list(range(10000, 0, -1))
    # 10s
    print(sol.count_by_bubble_sort(heights))
    print(time.time()-start_time)

    start_time = time.time()
    heights = list(range(500000, 0, -1))
    # 45s
    print(sol.count_by_bisecting(heights))
    print(time.time()-start_time)

    start_time = time.time()
    heights = list(range(500000, 0, -1))
    # 1.76s
    print(sol.count_by_merge_sort(heights))
    print(time.time()-start_time)