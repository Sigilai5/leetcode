# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.depth(root)
        return self.max_diameter

    def depth(self, node: Optional[TreeNode]) -> int:
        if not node: return 0

        left = self.depth(node.left)
        right = self.depth(node.right)

        self.max_diameter = max(self.max_diameter, left + right) 

        return max(left,right) + 1

        # SC -> O(1)
        # TC -> O(N)