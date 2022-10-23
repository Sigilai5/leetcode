public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
     int count = 0;
     int check = 1;
     for(int i = 0; i < 32; i++){
        if((n & check) != 0){
            count++;
        }
         
        check = check << 1; 
     } 
    
     return count;
       
    }
}


//Space Complexity: O(1)
//Time Complexity: O(32) -> O(1)