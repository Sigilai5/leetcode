"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        stack = []  # LIFO
        curr = head

        while curr:
            if curr.child:
                if curr.next:
                    stack.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            
            if curr.next == None and len(stack) != 0:
                curr.next = stack.pop()
                curr.next.prev = curr
                curr.child = None 

            curr = curr.next
        
        return head
                
        
