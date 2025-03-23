# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root

        queue = deque()

        queue.append(root)

        while queue:
            level_node = queue.popleft()

            hold = level_node.left
            level_node.left = level_node.right
            level_node.right = hold

            if level_node.left:
                queue.append(level_node.left)
            
            if level_node.right:
                queue.append(level_node.right)
        

        return root
        