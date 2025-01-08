# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        prev = None
        curr = head

        while curr:
            hold = curr.next
            curr.next = prev
            prev = curr
            curr = hold
        
        return prev

        # SC -> O(1)
        # TC -> O(N)