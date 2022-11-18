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
    public List<Integer> rightSideView(TreeNode root) {
        if(root == null) return new ArrayList();
        
        
        List<Integer> result = new ArrayList();
        Queue<TreeNode> queue = new LinkedList();
        
        queue.add(root); //[1]
            
        while(!queue.isEmpty()){
            int levelSize = queue.size();
            
            for(int i = 0; i< levelSize;i++){
                TreeNode currentLevel = queue.poll();
                if(i == levelSize - 1){
                    result.add(currentLevel.val);
                }
                
                if(currentLevel.left != null){
                    queue.add(currentLevel.left);
                }
                
                if(currentLevel.right != null){
                    queue.add(currentLevel.right);
                }
                
                
            }
            
            
        }    
        
        return result;
        
    }
}