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
        /*ITERATIVE APPROACH  */
        if(root == null) return root;
        Queue<TreeNode> nodes = new LinkedList<>();
        nodes.add(root);
        while(!nodes.isEmpty()){
            TreeNode rootNode = nodes.poll();
            
            TreeNode hold = rootNode.left;
            rootNode.left = rootNode.right;
            rootNode.right = hold;
            
            if(rootNode.left != null){
                nodes.add(rootNode.left);
            }
            
            if(rootNode.right != null){
                nodes.add(rootNode.right);
            }
           
        }
        
        return root;
        
        
        
        //Space complexity-> O(n), since we are use a Queue data store.
        //Time complexity-> O(n) since we are traversing through the height of the tree.
        
          /*RECURSIVE APPROACH*/
//        if(root == null) return root;
        
//        TreeNode hold = root.right;
//        root.right = root.left; 
//        root.left = hold;
        
//        invertTree(root.left);
//        invertTree(root.right);
        
//        return root; 
        
        
    }
}

//Space complexity-> O(1), since we are only shifting pointers.
//Time complexity-> O(h) since we are traversing through the height of the tree.