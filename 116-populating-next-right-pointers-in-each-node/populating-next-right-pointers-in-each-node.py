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
        if not root: return root

        queue = deque()

        queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left != None and node.right != None:
                node.left.next = node.right

            if node.right != None and node.next != None:
                node.right.next = node.next.left

            if node.right:
                queue.append(node.right)
            
            if node.left:
                queue.append(node.left)
        
        return root


        # SC -> O(N)
        # TC -> O(N)
                

        