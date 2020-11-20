# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1 = p2 = ret = head
        for _ in range(n):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        p2.val = -1
        if ret.val == -1: return ret.next

        p1 = head.next
        while True:
            if p1.val == -1:
                head.next = p1.next
                return ret
            head = head.next
            p1 = p1.next
