# -*- coding:utf-8 -*-


"""ACCEPT"""

# 运行时间：71ms
# 占用内存：5704k


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 前序遍历序列 {1,2,4,7,3,5,6,8}
# 中序遍历序列 {4,7,2,1,5,3,8,6}

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here

        root = pre[0]
        left_subtree_tin = tin[:tin.index(root)]
        right_subtree_tin = tin[tin.index(root)+1:]

        left_subtree_pre = []
        right_subtree_pre = []
        for node in pre[1:]:
            if node in left_subtree_tin:
                left_subtree_pre.append(node)
            else:
                right_subtree_pre.append(node)

        assert set(left_subtree_pre) == set(left_subtree_tin)
        assert set(right_subtree_pre) == set(right_subtree_tin)

        rc_tree = TreeNode(root)
        if left_subtree_pre:
            rc_tree.left = self.reConstructBinaryTree(left_subtree_pre, left_subtree_tin)
        if right_subtree_pre:
            rc_tree.right = self.reConstructBinaryTree(right_subtree_pre, right_subtree_tin)

        return rc_tree

if __name__ == "__main__":
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]

    sol = Solution()
    rc_tree = sol.reConstructBinaryTree(pre, tin)
    print(rc_tree.val)
    print(rc_tree.left.val)
    print(rc_tree.right.val)
    print(rc_tree.left.left.val)
    print(rc_tree.right.left.val)
    print(rc_tree.right.right.val)
    print(rc_tree.right.right.left.val)