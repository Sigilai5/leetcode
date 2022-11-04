/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        /*BFS Iteratively*/
        if(root == null) return root;
        Queue<Node> nodes = new LinkedList();
        
        nodes.add(root);
        
        while(!nodes.isEmpty()){
            Node head = nodes.poll();
            
            if(head.left != null){ 
                head.left.next = head.right;
            }
            
            if(head.right != null && head.next != null){
                head.right.next = head.next.left;
            }
            
            if(head.left != null && head.right != null){
                 nodes.add(head.left);
                nodes.add(head.right);
            }
           
            
            
        }
        
        
        return root;
        
        
        /*DFS Recursively*/
//         if(root == null) return root;
        
//         if(root.left != null){
//             root.left.next = root.right;
//         }
        
//         if(root.right != null && root.next != null){
//             root.right.next = root.next.left;
//         }
        
//         connect(root.left);
//         connect(root.right);
        
//         return root;
        
    }
    
    //Space Complexity -> O(1)
    //Time Complexity -> O(h)
}