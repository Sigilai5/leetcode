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
        if(root == null) return new ArrayList();
        List<List<Integer>> result = new ArrayList();
        Queue<TreeNode> queue = new LinkedList();
        boolean leftToRight = true;
        
        queue.add(root); //Queue to perform BFS iteratively level by level
        
        while(!queue.isEmpty()){
           List<Integer> levelList = new ArrayList(); // Level list    
           int levelSize = queue.size(); // [9,20] -> 2
           
           for(int i = 0; i<levelSize;i++){
               TreeNode currentLevel = queue.remove(); //Removing the nodes in queue [9,20]
               if(leftToRight == true){
                  levelList.add(currentLevel.val);  //Left to Right  [9,20]
               }else{
                   levelList.add(0,currentLevel.val);  //Right to Left
               }

               if(currentLevel.left != null){
                   queue.add(currentLevel.left);  // [9]
               } 

                if(currentLevel.right != null){
                   queue.add(currentLevel.right);  // [9,20]
               }

               }    

          
            result.add(levelList);  //[[3],[9,20]]
            leftToRight = !leftToRight; // false
        
        }
        
        
        return result;
        
        
                
    }
    
}


