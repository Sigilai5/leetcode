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
        
        Queue<TreeNode> tree_nodes = new LinkedList<TreeNode>();
        tree_nodes.add(root);
        while(!tree_nodes.isEmpty()){  //This ensures that all the child nodes have been inverted accordingly
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