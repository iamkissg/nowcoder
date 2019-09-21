import sys

# 100% passed

class Solution:
    def __init__(self, apple_heap):
        self.heaps = [0]
        for ah in apple_heap:
            self.heaps.append(self.heaps[-1]+ah)

        # 超过内存使用限制, 30%
        # self.heaps = {0: 0}
        # no = 0
        # for i, ah in enumerate(apple_heap, start=1):
        #     self.heaps.update({j: i for j in range(no+1, no+ah+1)})
        #     no += ah

    def which_heap(self, q):
        # return self.heaps[q]
        start, end = 0, len(self.heaps)-1

        while start < end-1:
            mid = (start+end)//2
            if self.heaps[mid-1] < q and q <= self.heaps[mid]:
                return mid
            elif self.heaps[mid] < q:
                start = mid
            elif self.heaps[mid] > q:
                end = mid
        else:
            return end


        # for i, h in enumerate(self.heaps):
        #     if q <= h:
        #         return i


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    apple_heap = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    qs = list(map(int, sys.stdin.readline().strip().split()))

    sol = Solution(apple_heap)
    for q in qs:
        print(sol.which_heap(q))