public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
//      int count = 0;
//      int check = 1;
//      for(int i = 0; i < 32; i++){
//         if((n & check) != 0){
//             count++;
//         }
         
//         check = check << 1; 
//      } 
    
//      return count;
        
    //Time Complexity: O(32) -> O(1)
    //Space Complexity: O(1)
        
    /*Method 2->Brian Kernighan Algorithm,*/
    int bitCount = 0;
    while(n != 0){
        n = n & (n-1); //The rightmost bit will be flipped each time until we end with a zero
        bitCount+=1;        
    }   
        
    return bitCount;
   
       
    }
}


