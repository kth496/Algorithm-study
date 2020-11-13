class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        dic = set()
        while head.next:
            if head in dic: return True
            dic.add(head)
            head = head.next
        return False
