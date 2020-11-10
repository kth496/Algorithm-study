class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        cur = ListNode()
        head = cur
        while True:
            if l1.val <= l2.val:
                cur.next, cur = l1, l1
                l1 = l1.next
            elif l1.val > l2.val:
                cur.next, cur = l2, l2
                l2 = l2.next
            if l1 is None:
                cur.next = l2
                break
            if l2 is None:
                cur.next = l1
                break

        return head.next
