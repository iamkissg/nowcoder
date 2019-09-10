# -*- coding:utf-8 -*-
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
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1

        
        if pHead1.val < pHead2.val:
            mHead = pHead1
            mHead.next = self.Merge(pHead1.next, pHead2)
        else:
            mHead = pHead2
            mHead.next = self.Merge(pHead1, pHead2.next)

        return mHead


if __name__ == "__main__":
    
    pHead1 = ListNode(1)
    pHead1.next = ListNode(2)
    pHead1.next.next = ListNode(3)

    pHead2 = ListNode(2)
    pHead2.next = ListNode(3)
    pHead2.next.next = ListNode(4)

    sol = Solution()

    print(sol.Merge(pHead1, pHead2))