"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

        stack = []

        1---2---3---7---8---11--12--9---10--4---5---6--NULL
                        
                        
                    

        

        output = [1,2,3,7,8,11,12,9,10,4,5,6]
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        stack = [] # LIFO
        curr = head

        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.next.prev = curr
                curr.child = None
            
            if curr.next is None and len(stack) > 0:
                curr.next = stack.pop()
                curr.next.prev = curr
                curr.child = None
            
            curr= curr.next
        
        return head

        # SC -> O(N)
        # TC -> O(N)
        

        