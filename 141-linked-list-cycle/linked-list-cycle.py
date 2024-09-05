# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False

        curr = head

        unique = set()

        while curr:
            if curr in unique:
                return True
            
            unique.add(curr)

            curr = curr.next
        
        return False
        
        # SC -> O(N)
        # TC -> O(N)