# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot2:
            return False

        result = False
        if pRoot1 and pRoot2:

            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)

        return result

    def DoesTree1HaveTree2(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False

        return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)


if __name__ == "__main__":
    t1 = TreeNode(8)
    t1.left = TreeNode(8)
    t1.left.left = TreeNode(9)
    t1.left.right = TreeNode(2)
    t1.left.right.left = TreeNode(4)
    t1.left.right.right = TreeNode(7)
    t1.right = TreeNode(7)


    t2 = TreeNode(8)
    t2.left = TreeNode(9)
    t2.right = TreeNode(2)

    sol = Solution()
    print(sol.HasSubtree(t1, t2))


