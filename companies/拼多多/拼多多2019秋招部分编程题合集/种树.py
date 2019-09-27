import sys

# 100%

'''
其实我感觉效率会比较低, 因为每次都检查剩下的树种是否合法, 判断太多了
'''

class Solution:

    def is_valid(self, n_trees):
        n_most = max(n_trees)
        n_rest = sum(n_trees) - n_most
        return False if n_most - 1 > n_rest else True

    def plant_tree(self, n_trees):
        if not self.is_valid(n_trees):
            return '-'

        result = []
        while sum(n_trees):
            for i, n in enumerate(n_trees):
                if n > 0 and (not result or i!=result[-1]-1) and self.is_valid(n_trees[:i]+[n-1]+n_trees[i+1:]):
                    result.append(i+1)
                    n_trees[i] -= 1
                    break
        return ' '.join(map(str, result))
        


if __name__ == "__main__":
    sol = Solution()

    N = int(sys.stdin.readline().strip())
    trees = list(map(int, sys.stdin.readline().strip().split()))

    print(sol.plant_tree(trees))
