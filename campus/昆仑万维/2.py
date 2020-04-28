import sys
from queue import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    

class Solution:
    def max_length_in_tree(self, root):
        myque = deque([root])

        res = []
        while myque:
            node = myque.popleft()

            if node.left:
                myque.append(node.left)
            if node.right:
                myque.append(node.right)

            left_max_dep = self.dfs(node.left, 0)
            right_max_dep = self.dfs(node.right, 0)
            res.append(right_max_dep + left_max_dep)
        return max(res)
    
    def dfs(self, node, cur_dep):
        if not node:
            return cur_dep
        
        left_dep = self.dfs(node.left, cur_dep+1)
        right_dep = self.dfs(node.right, cur_dep+1)
        
        return max(left_dep, right_dep)

    def construct_tree_from_array(self, tree_arr):
        root = TreeNode(tree_arr.pop(0))
        myque = deque([root])

        while tree_arr:
            node = myque.popleft()

            left = tree_arr.pop(0)
            node.left = TreeNode(left) if left != -1 else None

            if tree_arr:
                right = tree_arr.pop(0)
                node.right = TreeNode(right) if right != -1 else None

            if node.left:
                myque.append(node.left)
            if node.right:
                myque.append(node.right)

        return root
            

if __name__ == "__main__":
    sol = Solution()
    tree_arr = list(map(int, input().split()))
    
    if not tree_arr or len(tree_arr) < 2:
        print(0)
    else:
        tree = sol.construct_tree_from_array(tree_arr)
        print(sol.max_length_in_tree(tree))