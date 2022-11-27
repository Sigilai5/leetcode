class Solution {
    public Node connect(Node root) {
     if(root == null) return root;
        
     Queue<Node> level = new LinkedList(); //FIFO [1]   [2,3]
     level.add(root); //[1]
        
     while(!level.isEmpty()){
         Node head = level.remove(); //[1]
         
         if(head.left != null && head.right != null){
             head.left.next = head.right;   //[2->3]
         }//done with left
         
         if(head.right != null && head.next != null){
             head.right.next = head.next.left;
         }
         
         
         if(head.left != null && head.right != null){
             level.add(head.left);
             level.add(head.right);
         }
         
     }
        
     
    return root;
        
        
   
        
    }       
}