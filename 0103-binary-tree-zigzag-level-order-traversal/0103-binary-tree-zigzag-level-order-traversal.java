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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
            List<List<Integer>> result = new ArrayList();
            if(root == null) return result;
    
            Queue<TreeNode> queue = new LinkedList();
            queue.add(root);
            boolean leftToRight = true;
            while(!queue.isEmpty()){
                int levelSize = queue.size();
                List<Integer> levelList = new ArrayList();
                                
                for(int i = 0; i < levelSize;i++){
                    TreeNode current = queue.poll();
                    if(leftToRight == true){
                        levelList.add(current.val);
                    }else{
                       levelList.add(0,current.val); 
                        
                    }
                    
                    if(current.left != null) queue.add(current.left);
                    if(current.right != null) queue.add(current.right);
                                        
                       
                    }
                
                    
                
                    leftToRight = !leftToRight;
                    result.add(levelList);
                           
                
                    
                     }
                
                     return result;                
            }
                
    }
