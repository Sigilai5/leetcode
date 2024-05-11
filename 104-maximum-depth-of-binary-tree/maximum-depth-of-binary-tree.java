/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if(root == null) return 0;

        Queue<TreeNode> queue = new LinkedList();

        queue.add(root);

        int maxDepth = 0;

        while(!queue.isEmpty()){

            int levelSize = queue.size();

            for(int i = 0; i < levelSize; i++){
                TreeNode level = queue.remove();

                if(level.left != null){
                    queue.add(level.left);
                }

                if(level.right != null){
                    queue.add(level.right);
                }

            }

            maxDepth += 1;
        }

        return maxDepth;
        
    }
}


// SC -> O(N)
// TC -> O(N)