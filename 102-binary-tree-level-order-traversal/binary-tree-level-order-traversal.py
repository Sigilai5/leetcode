# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = deque()

        result = []

        queue.append(root)

        while queue:
            current_level = []
            for i in range(len(queue)):
                current_node = queue.popleft()
                current_level.append(current_node.val)  

                if current_node.left:
                    queue.append(current_node.left)
                
                if current_node.right:
                    queue.append(current_node.right)
            
            result.append(current_level)
        
        return result

            
            
    # SC -> O(N)
    # TC -> O(N)

        