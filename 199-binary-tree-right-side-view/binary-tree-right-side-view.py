# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        result = []

        while queue:
            size = len(queue)
            right = size - 1

            for i in range(size):
                curr = queue.popleft()
                if i == right:
                    result.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)
        
        return result

        # SC -> O(N)