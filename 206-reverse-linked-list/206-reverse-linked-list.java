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
    public ListNode reverseList(ListNode head) {
       if(head == null) return head;
       
        
        ListNode prevNode = null;
        ListNode nextNode = null;
        ListNode currentNode = head;
        
        
        while(currentNode != null){
            nextNode = currentNode.next;
            currentNode.next = prevNode;
            prevNode = currentNode;
            currentNode = nextNode;
            
        }
        
        
        return prevNode;
        
       //Space Complextity O(1) Since we are using pointers.
       //Time Complextity O(n)
        
       
    }
}