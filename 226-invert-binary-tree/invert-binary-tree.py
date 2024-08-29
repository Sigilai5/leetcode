# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        queue = deque()
        queue.append(root)

        while queue:
            queue_size = len(queue)

            for i in range(queue_size):
                current = queue.popleft()

                hold = current.left
                current.left = current.right
                current.right = hold

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)

        
        return root
    
    # SC -> O(N)
    # TC -> O(N) 
