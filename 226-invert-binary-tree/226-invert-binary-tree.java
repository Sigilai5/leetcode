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
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return root;
        
        
        TreeNode hold = root.left;
        root.left = root.right;
        root.right = hold;
        
        invertTree(root.left);
        invertTree(root.right);
        
        return root;
    }
}

//Space complexity-> O(1), since we are only shifting pointers.
//Time complexity-> O(n) since we are traversing through the tree.