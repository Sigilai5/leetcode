/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
       if(head == null) return head;
        
        ListNode dummyNode = new ListNode();
        dummyNode.next = head;
        ListNode prevNode = dummyNode;
        ListNode currentNode = head;
        
        
        while(currentNode != null){
            if(currentNode.val == val){
                prevNode.next = currentNode.next;
            }else{
                prevNode = currentNode;
            }
            
            currentNode = currentNode.next;
            
        }
      
        
        return dummyNode.next;
    }
}


//Space Complexity = O(1) since we are just shifting pointers
//Time  Complexity = O(n) since we are traversing through the linked lists
