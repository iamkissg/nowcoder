from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_paths(self, root: TreeNode, expect_value: int) -> List[str]:
        if not root:
            return None

        paths = [p for p in self.DFS(root) if sum(p) == expect_value]
        if not paths:
            return -1

        return sorted(paths, key=lambda x: len(x))
        
    
    def DFS(self, root):
        # 不能这么算, 会多出路径来的, 指向了空
        # if not root:
        #     return [[]]

        if root.left is None and root.right is None:
            return [[root.val]]

        paths = []
        if root.left is not None:
            paths.extend([[root.val]+p for p in self.DFS(root.left)])
        if root.right is not None:
            paths.extend([[root.val]+p for p in self.DFS(root.right)])
        return paths


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(1)
    root.right = TreeNode(3)

    sol = Solution()
    print(sol.find_paths(root, 4))
