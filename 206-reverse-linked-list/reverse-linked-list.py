# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        # [1,2]
        curr = head
        prev = None

        while curr:
            hold = curr.next
            curr.next = prev
            prev = curr
            curr = hold
            
        
        return prev