# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        p1, p2 = head, head
        while p1.next and p1.next.next:
            p1 = p1.next.next
            p2 = p2.next
            
            if p1 == p2:
                return True
        return False