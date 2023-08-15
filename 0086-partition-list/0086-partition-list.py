# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        large = []
        small = []
        while head:
            if head.val >= x:
                large.append(head.val)
            else:
                small.append(head.val)
            head = head.next

        small += large
        
        sol = None
        for i in range(len(small)-1, -1, -1):
            tmp = ListNode(val=small[i], next=sol)
            sol = tmp
        
        return sol
        