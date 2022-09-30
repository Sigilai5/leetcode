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
        /*ITERATIVE APPORACH*/
        if(root == null) return root;
        
        Queue<TreeNode> tree_nodes = new LinkedList<TreeNode>();  //We use que for level order traversal.
        tree_nodes.add(root); // Prevent the queue from being empty at first.
        while(!tree_nodes.isEmpty()){//making sure its empty at the end to escape the condition and return the root once invertion is done in both sides.
            TreeNode temp = tree_nodes.poll(); 
            
            TreeNode hold = temp.left;
            temp.left = temp.right;
            temp.right = hold;
            
            if(temp.left != null){
                tree_nodes.add(temp.left);
            }
            
             if(temp.right != null){
                tree_nodes.add(temp.right);
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