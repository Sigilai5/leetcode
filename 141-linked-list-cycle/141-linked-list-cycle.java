/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head == null) return false;
        
        ListNode slowNode = head;
        ListNode fastNode = head.next;
        
        while(slowNode != null && fastNode != null && fastNode.next != null){
            if(slowNode == fastNode){
                return true;
                
            }
            
            slowNode = slowNode.next;
            fastNode = fastNode.next.next;
            
        }
        
        return false;
        
    }
}