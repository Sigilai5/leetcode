"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        queue = deque()
        queue.append(root)

        while queue:
            for i in range(len(queue)):
                current_level = queue.popleft()
                
                if current_level.left:
                    current_level.left.next = current_level.right
                
                if current_level.right and current_level.next:
                    current_level.right.next = current_level.next.left
            
                if current_level.left:
                    queue.append(current_level.left)
                
                if current_level.right:
                    queue.append(current_level.right)
        
        return root
    
    # SC -> O(N)
    # TC -> O(N)
