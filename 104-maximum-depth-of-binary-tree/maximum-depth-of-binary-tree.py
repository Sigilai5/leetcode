# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        queue = deque()

        queue.append(root)

        max_depth = 0

        while queue:
            for i in range(len(queue)):
                current_level = queue.popleft()

                if current_level.left: 
                    queue.append(current_level.left)

                if current_level.right:
                    queue.append(current_level.right)
            max_depth+=1
        

        return max_depth
        