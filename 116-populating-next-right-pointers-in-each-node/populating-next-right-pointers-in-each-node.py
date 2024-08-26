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
            size = len(queue)

            for i in range(size):
                current = queue.popleft()

                if current.left != None and current.right != None:
                    current.left.next = current.right
                
                if current.right != None and current.next != None:
                    current.right.next = current.next.left
                

                if current.left:
                    queue.append(current.left)
                
                if current.right:
                    queue.append(current.right)
        
        return root


    # SC -> O(N)
    # TC -> O(N)
        