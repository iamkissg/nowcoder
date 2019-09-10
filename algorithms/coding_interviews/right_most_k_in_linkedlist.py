# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):

        if not head:
            return None

        if k < 1:
            return None

        p1 = head
        p2 = head
        for _ in range(k-1):
            if p2.next is None:
                return None
            p2 = p2.next
        
        while p2.next is not None:
            p1 = p1.next
            p2 = p2.next

        # 其实应该是 p1.val
        return p1


if __name__ == "__main__":
    sol = Solution()

    ll = ListNode(1)
    ll.next = ListNode(2)
    ll.next.next = ListNode(3)
    ll.next.next.next = ListNode(4)
    ll.next.next.next.next = ListNode(5)

    print(sol.FindKthToTail(ll, 1))