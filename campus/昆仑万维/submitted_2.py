import sys

class Solution:
    def max_length_in_tree(self, root):
        if not root or len(root) < 2:
            return 0

        n = len(root)
        l, r = 1, 3
        left_depth, right_depth = 0, 0
        while l < n:
            mid = l + (r-l) // 2
            if any(a!=-1 for a in root[l: mid]):
                left_depth += 1
            if any(a!=-1 for a in root[mid: r]):
                right_depth += 1
            l, r = r, r*2+1
        return left_depth + right_depth

if __name__ == "__main__":
    sol = Solution()
    tarr = list(map(int, input().split()))
    print(sol.max_length_in_tree(tarr))