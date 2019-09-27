import sys 

'''
区间选点问题, 看过来比较常规的做法是: 按端点排序(右端) + 贪心算法, 总是选择右端点, 当区间不重叠时, 再从下一个区间选点
'''

class Solution:

    def times_to_select(self, pairs):
        if not pairs:
            return 0

        pairs = sorted(pairs, key=lambda t: t[1])

        end_point = pairs[0][1]
        points = {end_point}
        for p in pairs[1:]:
            if p[0] <= end_point:
                continue
            end_point = p[1]
            points.add(end_point)
        return len(points)*2



if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    pairs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    sol = Solution()
    print(sol.times_to_select(pairs))

'''
5
62 69
46 73
42 57
45 49
72 96

6
'''