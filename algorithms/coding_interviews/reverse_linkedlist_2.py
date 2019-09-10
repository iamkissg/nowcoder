# -*- coding:utf-8 -*-
from copy import deepcopy, copy


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        vals = str(self.val)
        p = self.next
        while p.next is not None:
            vals += str(p.val)
            p = p.next
        else:
            vals += str(p.val)
        return vals


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead:
            return None

        if pHead.next is None:
            return pHead

        dummy_node = ListNode(0)
        rHead = copy(pHead)    # 表头作为另一个的表尾
        rHead.next = None      # 表尾
        rll = pHead.next       # 从第二个块开始

        while rll.next is not None:
            dummy_node.next = rll.next  # 哑节点暂存后续链表
            rll.next = rHead            # 回指前一个表块
            rHead = rll                 # rHead 指向反转链表的表头
            rll = dummy_node.next
        else:
            rll.next = rHead
            rHead = rll

        return rHead

if __name__ == "__main__":
    pHead = ListNode(1)
    pHead.next = ListNode(2)
    pHead.next.next = ListNode(3)

    sol = Solution()

    print(sol.ReverseList(pHead))

