# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        result = []
        queue = deque()
        queue.append([0,root])
        visited_levels = set()

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                level,curr_node = queue.popleft()
                if level not in visited_levels:
                    result.append(curr_node.val)
                    visited_levels.add(level)

                if curr_node.right:
                    queue.append([level + 1, curr_node.right])
                if curr_node.left:
                    queue.append([level + 1, curr_node.left])
        
        return result