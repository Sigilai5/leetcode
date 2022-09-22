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
        
        
        TreeNode currentNode = root;
        
        TreeNode hold = currentNode.left;
        currentNode.left = currentNode.right;
        currentNode.right = hold;
        
        invertTree(root.left);
        invertTree(root.right);

       
     
        
        return root;
        
    }
}