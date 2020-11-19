class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def make_node(self, carry: int, *args: int):
        acc = carry
        for val in args:
            acc += val
        c = 1 if acc > 9 else 0
        new_node = ListNode(acc % 10)
        return c, new_node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur_node = ListNode()
        carry = 0

        while l1 and l2:
            carry, new_node = self.make_node(carry, l1.val, l2.val)
            cur_node.next = new_node
            cur_node = new_node
            l1 = l1.next
            l2 = l2.next

        remain = l1 if l1 else l2

        while remain:
            carry, new_node = self.make_node(carry, remain.val)
            cur_node.next = new_node
            cur_node = new_node
            remain = remain.next

        if carry:
            cur_node.next = ListNode(1)
            
        return head.next
